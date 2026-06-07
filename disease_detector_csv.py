"""
Disease Detection using CSV Dataset
Loads disease-symptoms-precautions-specialist.csv and provides disease prediction
based on symptom matching with support for precautions, urgency levels, and specialists.
"""

import pandas as pd
import csv
from difflib import SequenceMatcher
from typing import List, Dict, Tuple, Optional
import os

class DiseaseDetectorCSV:
    """Disease detection engine using CSV dataset"""
    
    def __init__(self, csv_path: str = 'disease-symptoms-precautions-specialist.csv'):
        """
        Initialize disease detector with CSV file
        
        Args:
            csv_path: Path to the CSV file
        """
        self.csv_path = csv_path
        self.disease_data = {}
        self.all_symptoms = set()
        self.disease_symptom_map = {}  # disease -> list of symptoms
        
        if os.path.exists(csv_path):
            self.load_csv_data()
        else:
            print(f"⚠️  CSV file not found: {csv_path}")
    
    def load_csv_data(self):
        """Load and parse CSV data into structured format"""
        try:
            df = pd.read_csv(self.csv_path)
            
            for _, row in df.iterrows():
                disease = row['disease'].strip()
                symptoms_str = row['symptoms'].strip()
                precautions_str = row['precautions'].strip()
                specialist = row['specialist'].strip()
                urgency = row['urgency'].strip()
                
                # Parse symptoms - they're comma-separated
                symptoms = [s.strip() for s in symptoms_str.split(',')]
                
                # Parse precautions
                precautions = [p.strip() for p in precautions_str.split(',')]
                
                # Store disease data
                self.disease_data[disease] = {
                    'symptoms': symptoms,
                    'precautions': precautions,
                    'specialist': specialist,
                    'urgency': urgency
                }
                
                # Track all symptoms and disease-symptom relationships
                for symptom in symptoms:
                    self.all_symptoms.add(symptom)
                    if symptom not in self.disease_symptom_map:
                        self.disease_symptom_map[symptom] = []
                    if disease not in self.disease_symptom_map[symptom]:
                        self.disease_symptom_map[symptom].append(disease)
            
            print(f"✓ Loaded {len(self.disease_data)} diseases")
            print(f"✓ Extracted {len(self.all_symptoms)} unique symptoms")
        
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
    
    def fuzzy_match_symptom(self, text: str, threshold: float = 0.6) -> List[Tuple[str, float]]:
        """
        Find symptoms using fuzzy matching
        
        Args:
            text: Symptom text to match
            threshold: Minimum similarity score (0-1)
            
        Returns:
            List of (symptom, score) tuples sorted by score
        """
        matches = []
        text_lower = text.lower().strip()
        
        for symptom in self.all_symptoms:
            symptom_lower = symptom.lower()
            ratio = SequenceMatcher(None, text_lower, symptom_lower).ratio()
            
            if ratio >= threshold:
                matches.append((symptom, ratio))
        
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches
    
    def extract_symptoms(self, symptom_list: List[str], fuzzy_threshold: float = 0.65) -> List[str]:
        """
        Extract and validate symptoms from user input
        
        Args:
            symptom_list: List of symptom strings
            fuzzy_threshold: Threshold for fuzzy matching
            
        Returns:
            List of validated symptom names
        """
        detected = []
        
        for symptom in symptom_list:
            symptom_lower = symptom.lower().strip()
            
            # Try exact match first
            exact_match = next((s for s in self.all_symptoms if s.lower() == symptom_lower), None)
            if exact_match:
                if exact_match not in detected:
                    detected.append(exact_match)
                continue
            
            # Try substring match
            substring_match = next((s for s in self.all_symptoms if symptom_lower in s.lower()), None)
            if substring_match:
                if substring_match not in detected:
                    detected.append(substring_match)
                continue
            
            # Try fuzzy match
            fuzzy_matches = self.fuzzy_match_symptom(symptom, threshold=fuzzy_threshold)
            if fuzzy_matches and fuzzy_matches[0][1] >= fuzzy_threshold:
                if fuzzy_matches[0][0] not in detected:
                    detected.append(fuzzy_matches[0][0])
        
        return detected
    
    def predict_diseases(self, symptoms: List[str], top_n: int = 5) -> List[Dict]:
        """
        Predict diseases based on symptoms
        
        Args:
            symptoms: List of symptom names (already validated)
            top_n: Number of top predictions to return
            
        Returns:
            List of disease predictions with confidence scores and details
        """
        if not symptoms:
            return []
        
        disease_scores = {}
        
        # Score each disease based on symptom overlap
        for disease, data in self.disease_data.items():
            disease_symptoms = set(s.lower() for s in data['symptoms'])
            user_symptoms = set(s.lower() for s in symptoms)
            
            # Calculate Jaccard similarity
            intersection = len(disease_symptoms & user_symptoms)
            union = len(disease_symptoms | user_symptoms)
            
            if union > 0:
                jaccard_score = intersection / union
                
                # Bonus: exact match is better
                exact_matches = intersection
                
                # Combined score: 70% Jaccard, 30% exact match count
                score = (0.7 * jaccard_score) + (0.3 * (exact_matches / max(len(disease_symptoms), len(user_symptoms))))
                
                if score > 0:
                    disease_scores[disease] = {
                        'score': score,
                        'matching_symptoms': list(disease_symptoms & user_symptoms),
                        'match_count': intersection,
                        'total_disease_symptoms': len(disease_symptoms)
                    }
        
        # Sort by score
        sorted_diseases = sorted(disease_scores.items(), key=lambda x: x[1]['score'], reverse=True)
        
        # Build response
        predictions = []
        for disease, data in sorted_diseases[:top_n]:
            disease_info = self.disease_data[disease]
            
            predictions.append({
                'disease': disease,
                'confidence': round(data['score'], 3),
                'confidence_percentage': f"{data['score']*100:.1f}%",
                'matching_symptoms': data['matching_symptoms'],
                'match_count': data['match_count'],
                'total_disease_symptoms': data['total_disease_symptoms'],
                'specialist': disease_info['specialist'],
                'urgency': disease_info['urgency'],
                'precautions': disease_info['precautions']
            })
        
        return predictions
    
    def get_disease_info(self, disease: str) -> Optional[Dict]:
        """Get full information about a disease"""
        return self.disease_data.get(disease)
    
    def get_all_symptoms_list(self) -> List[str]:
        """Get sorted list of all symptoms"""
        return sorted(list(self.all_symptoms))
    
    def get_all_diseases_list(self) -> List[str]:
        """Get sorted list of all diseases"""
        return sorted(list(self.disease_data.keys()))


# Create global instance
disease_detector = None

def initialize_detector(csv_path: str = 'disease-symptoms-precautions-specialist.csv') -> DiseaseDetectorCSV:
    """Initialize global disease detector instance"""
    global disease_detector
    disease_detector = DiseaseDetectorCSV(csv_path)
    return disease_detector

def get_detector() -> DiseaseDetectorCSV:
    """Get global disease detector instance"""
    global disease_detector
    if disease_detector is None:
        disease_detector = initialize_detector()
    return disease_detector
