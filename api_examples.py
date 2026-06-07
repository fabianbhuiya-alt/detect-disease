"""
Example: How to use the Disease Prediction API

Run this AFTER:
1. Running 01_Preprocess_New_Dataset.ipynb
2. Running 02_Train_Model.ipynb
3. Running app_new.py in another terminal
"""

import requests
import json

# API URL
BASE_URL = "http://localhost:5000"

print("="*60)
print("DISEASE PREDICTION API - USAGE EXAMPLES")
print("="*60)

# Example 1: Get available symptoms
print("\n1. Get Available Symptoms")
print("-" * 60)
response = requests.get(f"{BASE_URL}/api/symptoms")
data = response.json()
print(f"Total symptoms available: {data['total']}")
print(f"First 5 symptoms:")
for i, symptom in enumerate(data['symptoms'][:5], 1):
    print(f"   {i}. {symptom}")
print("   ...")

# Example 2: Get available diseases
print("\n2. Get Available Diseases")
print("-" * 60)
response = requests.get(f"{BASE_URL}/api/diseases")
data = response.json()
print(f"Total diseases: {data['total']}")
print(f"First 5 diseases:")
for i, disease in enumerate(data['diseases'][:5], 1):
    print(f"   {i}. {disease}")
print("   ...")

# Example 3: Make a prediction
print("\n3. Make a Disease Prediction")
print("-" * 60)

# Get all symptoms first
response = requests.get(f"{BASE_URL}/api/symptoms")
all_symptoms = response.json()['symptoms']

# Create a symptoms dictionary with random selection
# In real use, you would get this from a form or user input
symptoms_dict = {}
for symptom in all_symptoms:
    symptoms_dict[symptom] = 0

# Select some symptoms (example: panic disorder symptoms)
selected_symptoms = [
    'anxiety and nervousness',
    'depression',
    'shortness of breath',
    'dizziness',
    'palpitations',
    'fear and phobia',
]

# Set selected symptoms to 1
for symptom in selected_symptoms:
    if symptom in symptoms_dict:
        symptoms_dict[symptom] = 1

print(f"Selected symptoms ({len(selected_symptoms)}):")
for i, symptom in enumerate(selected_symptoms, 1):
    print(f"   {i}. {symptom}")

# Make prediction
print("\nMaking prediction...")
response = requests.post(
    f"{BASE_URL}/predict",
    json={"symptoms": symptoms_dict}
)

if response.status_code == 200:
    result = response.json()
    
    if result['success']:
        print("\n✓ PREDICTION RESULT:")
        print(f"   Disease: {result['predicted_disease']}")
        print(f"   Confidence: {result['confidence_percentage']}")
        
        print(f"\n   Recommended Specialists:")
        for i, specialist in enumerate(result['recommended_specialists'], 1):
            print(f"      {i}. {specialist}")
        
        print(f"\n   Top Predictions:")
        for i, pred in enumerate(result['top_predictions'], 1):
            print(f"      {i}. {pred['disease']} - {pred['probability']*100:.1f}%")
    else:
        print(f"✗ Error: {result['error']}")
else:
    print(f"✗ HTTP Error {response.status_code}")
    print(response.text)

# Example 4: Test with list of symptoms instead of dict
print("\n4. Alternative: Using Symptom List Instead of Dict")
print("-" * 60)

symptoms_list = [
    'anxiety and nervousness',
    'depression',
    'shortness of breath',
]

print(f"Selected symptoms: {symptoms_list}")

response = requests.post(
    f"{BASE_URL}/predict",
    json={"symptoms": symptoms_list}
)

if response.status_code == 200:
    result = response.json()
    if result['success']:
        print(f"\nPredicted Disease: {result['predicted_disease']}")
        print(f"Confidence: {result['confidence_percentage']}")
    else:
        print(f"Error: {result['error']}")

# Example 5: Health check
print("\n5. Health Check Endpoint")
print("-" * 60)

response = requests.get(f"{BASE_URL}/health")
health = response.json()
print(f"Status: {health['status']}")
print(f"Model loaded: {health['model_loaded']}")
print(f"Symptoms available: {health['symptoms_available']}")
print(f"Diseases available: {health['diseases_available']}")

print("\n" + "="*60)
print("✓ API Examples Complete")
print("="*60)

# Example usage in Python code:
print("\n📝 Example: How to integrate in your code:\n")
print("""
import requests

def predict_disease(symptoms_dict):
    '''
    Predict disease from symptoms
    
    Args:
        symptoms_dict: Dict of {symptom_name: 0 or 1}
    
    Returns:
        dict with disease, confidence, specialists
    '''
    response = requests.post(
        "http://localhost:5000/predict",
        json={"symptoms": symptoms_dict}
    )
    return response.json()

# Usage:
result = predict_disease({
    'anxiety and nervousness': 1,
    'depression': 1,
    'shortness of breath': 1,
    # ... other symptoms
})

if result['success']:
    print(f"Disease: {result['predicted_disease']}")
    print(f"Confidence: {result['confidence_percentage']}")
    print(f"Specialists: {result['recommended_specialists']}")
""")
