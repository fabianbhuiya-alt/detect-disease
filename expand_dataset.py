import pandas as pd
import numpy as np
import os

# Comprehensive medical symptom database
COMPREHENSIVE_SYMPTOMS = {
    'Fungal infection': [
        'itching', 'skin_rash', 'nodal_skin_eruptions', 'dischromic_patches',
        'skin_peeling', 'redness', 'burning_sensation', 'scaling', 'crusting',
        'blistering', 'pustules', 'maceration', 'erythema', 'pruritus',
        'vesicles', 'papules', 'nail_involvement', 'hair_loss', 'skin_thickening'
    ],
    'Allergy': [
        'sneezing', 'continuous_sneezing', 'itching', 'pruritus_ani', 'skin_rash',
        'watery_eyes', 'nasal_congestion', 'throat_irritation', 'swollen_lymph',
        'runny_nose', 'facial_puffiness', 'red_eyes', 'histamine_release',
        'anaphylaxis', 'edema', 'urticaria', 'rhinitis', 'conjunctivitis',
        'angioedema', 'allergic_asthma', 'laryngeal_edema', 'oral_allergy_syndrome'
    ],
    'GERD': [
        'acidity', 'stomach_pain', 'heartburn', 'reflux', 'regurgitation',
        'nausea', 'difficulty_swallowing', 'chest_discomfort', 'belching',
        'bloating', 'vomiting', 'upper_abdominal_pain', 'erosion_teeth',
        'chronic_cough', 'hoarseness', 'bad_breath', 'esophageal_spasm',
        'chest_pain', 'dyspepsia', 'gastritis', 'food_regurgitation'
    ],
    'Chronic_cholestasis': [
        'itching', 'skin_rash', 'fatigue', 'jaundice', 'dark_urine',
        'pale_stool', 'abdominal_pain', 'nausea', 'vomiting', 'loss_appetite',
        'weight_loss', 'hepatomegaly', 'splenomegaly', 'ascites', 'edema',
        'spider_angiomas', 'xanthomas', 'pruritus', 'clay_colored_stools',
        'hepatic_encephalopathy', 'portal_hypertension'
    ],
    'Drug_reaction': [
        'skin_rash', 'itching', 'redness', 'burning', 'swelling',
        'blistering', 'fever', 'chills', 'malaise', 'lymphadenopathy',
        'facial_swelling', 'throat_swelling', 'difficulty_breathing', 'hypotension',
        'tachycardia', 'nausea', 'vomiting', 'diarrhea', 'abdominal_pain',
        'photosensitivity', 'serum_sickness', 'stevens_johnson_syndrome'
    ],
    'Peptic_ulcer_disease': [
        'stomach_pain', 'abdominal_pain', 'acidity', 'nausea', 'vomiting',
        'heartburn', 'loss_appetite', 'blood_vomiting', 'black_stool',
        'bloating', 'belching', 'early_satiety', 'gastric_ulcer', 'duodenal_ulcer',
        'epigastric_tenderness', 'anemia', 'weight_loss', 'melena', 'hematemesis'
    ],
    'AIDS': [
        'fever', 'chills', 'fatigue', 'weight_loss', 'loss_appetite',
        'diarrhea', 'night_sweats', 'cough', 'shortness_breath', 'skin_rash',
        'lymphadenopathy', 'oral_thrush', 'pneumonia', 'tuberculosis', 'kaposi_sarcoma',
        'cryptococcosis', 'toxoplasmosis', 'cmv', 'opportunistic_infections', 'cd4_count_low'
    ],
    'Diabetes': [
        'polyuria', 'polydipsia', 'fatigue', 'weight_loss', 'increased_appetite',
        'blurred_vision', 'headache', 'slow_healing', 'frequent_infections',
        'tingling_extremities', 'neuropathy', 'nephropathy', 'retinopathy',
        'sweating', 'weakness', 'muscle_cramps', 'ketoacidosis', 'hyperglycemia',
        'hypoglycemia', 'diabetic_foot', 'dark_skin_patches'
    ],
    'Gastroenteritis': [
        'vomiting', 'nausea', 'diarrhea', 'abdominal_pain', 'stomach_pain',
        'cramps', 'fever', 'chills', 'watery_stool', 'bloody_stool',
        'dehydration', 'headache', 'muscle_aches', 'loss_appetite', 'weakness',
        'fatigue', 'malaise', 'tenesmus', 'mucus_stool', 'food_poisoning'
    ],
    'Bronchial_asthma': [
        'cough', 'shortness_breath', 'wheezing', 'chest_tightness', 'chest_pain',
        'breathing_difficulty', 'fast_breathing', 'fatigue', 'sleep_disturbance',
        'difficulty_speaking', 'pale_lips', 'excessive_sweating', 'asthma_attack',
        'wheezing_sound', 'hyperventilation', 'acute_exacerbation', 'status_asthmaticus'
    ],
    'Hypertension': [
        'headache', 'dizziness', 'fatigue', 'shortness_breath', 'nosebleed',
        'chest_pain', 'vision_problems', 'difficulty_concentrating', 'sweating',
        'nausea', 'anxiety', 'insomnia', 'high_bp', 'palpitations', 'flushed_face',
        'difficulty_sleeping', 'blood_in_urine', 'severe_headache'
    ],
    'Migraine': [
        'headache', 'acidity', 'vomiting', 'nausea', 'aura', 'visual_disturbance',
        'photosensitivity', 'phonophobia', 'throbbing_pain', 'unilateral_pain',
        'neck_stiffness', 'fatigue', 'dizziness', 'weakness', 'tingling',
        'numbness', 'confusion', 'slurred_speech', 'light_sensitivity'
    ],
    'Cervical_spondylosis': [
        'neck_pain', 'shoulder_pain', 'back_pain', 'numbness', 'weakness',
        'tingling', 'headache', 'dizziness', 'loss_balance', 'incoordination',
        'tremor', 'muscle_weakness', 'spasticity', 'hyperreflexia', 'neuropathy',
        'radiculopathy', 'myelopathy', 'limited_neck_movement'
    ],
    'Paralysis': [
        'weakness', 'loss_strength', 'inability_move', 'muscle_atrophy',
        'spasticity', 'flaccidity', 'hyperreflexia', 'hyporeflexia', 'spasm',
        'contracture', 'tremor', 'rigidity', 'loss_sensation', 'numbness',
        'tingling', 'pain', 'cramping', 'fasciculation'
    ],
    'Jaundice': [
        'yellowing_eyes', 'yellow_urine', 'pale_stool', 'itching', 'fatigue',
        'nausea', 'vomiting', 'abdominal_pain', 'loss_appetite', 'weight_loss',
        'fever', 'dark_urine', 'hepatomegaly', 'splenomegaly', 'ascites',
        'hyperbilirubinemia', 'acholic_stool', 'hepatic_dysfunction'
    ],
    'Malaria': [
        'fever', 'chills', 'sweating', 'headache', 'muscle_pain', 'fatigue',
        'nausea', 'vomiting', 'diarrhea', 'abdominal_pain', 'jaundice',
        'hepatosplenomegaly', 'anemia', 'thrombocytopenia', 'acute_kidney_injury',
        'cerebral_malaria', 'severe_anemia', 'pulmonary_edema', 'shock'
    ],
    'Tuberculosis': [
        'cough', 'chest_pain', 'blood_cough', 'shortness_breath', 'fever',
        'chills', 'night_sweats', 'weight_loss', 'fatigue', 'loss_appetite',
        'malaise', 'hemoptysis', 'dyspnea', 'wheezing', 'lung_cavitation',
        'consolidation', 'lymphadenitis', 'extrapulmonary_tb'
    ],
}

print("Loading current dataset...")
df = pd.read_csv('Data/dataset.csv')
print(f"Current shape: {df.shape}")

# Get diseases
diseases = df['Disease'].unique()
print(f"Number of diseases: {len(diseases)}")

# Calculate how many symptom columns we need for ~1000 unique symptoms
# Strategy: Add more columns (e.g., 40 columns total) with diverse symptoms
total_symptom_cols = 40

print(f"\nExpanding dataset to {total_symptom_cols} symptom columns...")

# Create expanded dataset
expanded_data = []

for idx, row in df.iterrows():
    disease = row['Disease']
    new_row = {'Disease': disease}
    
    # Get predefined symptoms for this disease or use generic ones
    if disease in COMPREHENSIVE_SYMPTOMS:
        disease_symptoms = COMPREHENSIVE_SYMPTOMS[disease]
    else:
        # Generic symptoms if not in our list
        disease_symptoms = [
            'fever', 'fatigue', 'cough', 'headache', 'nausea',
            'chest_pain', 'weight_loss', 'weakness', 'chills', 'vomiting'
        ]
    
    # Get existing symptoms from original data
    existing_symptoms = [row[f'Symptom_{i}'] for i in range(1, 18) if pd.notna(row[f'Symptom_{i}'])]
    
    # Combine and shuffle
    all_available = list(set(disease_symptoms + existing_symptoms))
    np.random.seed(hash(disease + str(idx)) % 2**32)  # Deterministic but varied
    np.random.shuffle(all_available)
    
    # Fill symptom columns
    for col_idx in range(1, total_symptom_cols + 1):
        if col_idx - 1 < len(all_available):
            new_row[f'Symptom_{col_idx}'] = all_available[col_idx - 1]
        else:
            new_row[f'Symptom_{col_idx}'] = np.nan
    
    expanded_data.append(new_row)

# Create new dataframe
df_expanded = pd.DataFrame(expanded_data)

# Save expanded dataset
print(f"Saving expanded dataset...")
df_expanded.to_csv('Data/dataset_expanded.csv', index=False)
print(f"✓ Saved to Data/dataset_expanded.csv")
print(f"  New shape: {df_expanded.shape}")

# Count unique symptoms
all_symptoms_set = set()
for col in [f'Symptom_{i}' for i in range(1, total_symptom_cols + 1)]:
    symptoms = df_expanded[col].dropna().unique()
    all_symptoms_set.update(symptoms)

print(f"\n✓ Total unique symptoms: {len(all_symptoms_set)}")
print(f"✓ Symptom columns: {total_symptom_cols}")

# Show sample
print("\nSample disease symptoms:")
for disease in list(diseases)[:3]:
    mask = df_expanded['Disease'] == disease
    symptoms = []
    for col in [f'Symptom_{i}' for i in range(1, total_symptom_cols + 1)]:
        symp = df_expanded[mask][col].iloc[0]
        if pd.notna(symp):
            symptoms.append(symp)
    print(f"{disease}: {', '.join(symptoms[:10])}...")
