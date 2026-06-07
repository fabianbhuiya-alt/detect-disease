#!/usr/bin/env python
"""Quick test of CSV disease detector"""

from disease_detector_csv import initialize_detector

print("="*60)
print("TESTING CSV DISEASE DETECTOR")
print("="*60)

detector = initialize_detector('disease-symptoms-precautions-specialist.csv')

print(f"\n✓ Total diseases: {len(detector.get_all_diseases_list())}")
print(f"✓ Total symptoms: {len(detector.get_all_symptoms_list())}")

print("\n" + "="*60)
print("TEST 1: Predicting from symptoms list")
print("="*60)

test_symptoms = ['fever', 'cough', 'sore throat']
validated = detector.extract_symptoms(test_symptoms)
print(f"Input symptoms: {test_symptoms}")
print(f"Validated: {validated}")

predictions = detector.predict_diseases(validated, top_n=3)
print(f"\nTop 3 predictions:")
for i, pred in enumerate(predictions[:3], 1):
    print(f"\n{i}. {pred['disease']}")
    print(f"   Confidence: {pred['confidence_percentage']}")
    print(f"   Specialist: {pred['specialist']}")
    print(f"   Urgency: {pred['urgency']}")
    print(f"   Matching symptoms: {pred['matching_symptoms']}")
    print(f"   Precautions: {pred['precautions'][:2]}...")  # First 2

print("\n" + "="*60)
print("TEST 2: Predicting from free text")
print("="*60)

text = "I have chest pain and shortness of breath"
words = text.lower().split()
validated2 = detector.extract_symptoms(words)
print(f"Input text: {text}")
print(f"Detected symptoms: {validated2}")

predictions2 = detector.predict_diseases(validated2, top_n=2)
print(f"\nTop predictions:")
for pred in predictions2:
    print(f"- {pred['disease']}: {pred['confidence_percentage']}")

print("\n" + "="*60)
print("ALL TESTS COMPLETED SUCCESSFULLY ✓")
print("="*60)
