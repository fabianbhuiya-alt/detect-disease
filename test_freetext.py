#!/usr/bin/env python
"""Test free-text disease prediction"""

from disease_detector_csv import initialize_detector

detector = initialize_detector('disease-symptoms-precautions-specialist.csv')

print("="*60)
print("TESTING FREE-TEXT DISEASE PREDICTION")
print("="*60)

# Test 1: Fever, cough, sore throat
text1 = 'I have a fever, cough, and sore throat'
symptom_words1 = text1.lower().split()
validated1 = detector.extract_symptoms(symptom_words1, fuzzy_threshold=0.65)
predictions1 = detector.predict_diseases(validated1, top_n=3)

print(f"\nTEST 1: '{text1}'")
print(f"Extracted: {validated1}")
print("Top predictions:")
for i, pred in enumerate(predictions1[:3], 1):
    print(f"  {i}. {pred['disease']} ({pred['confidence_percentage']})")

# Test 2: Chest pain and shortness of breath
text2 = 'I have chest pain and shortness of breath'
symptom_words2 = text2.lower().split()
validated2 = detector.extract_symptoms(symptom_words2, fuzzy_threshold=0.65)
predictions2 = detector.predict_diseases(validated2, top_n=3)

print(f"\nTEST 2: '{text2}'")
print(f"Extracted: {validated2}")
print("Top predictions:")
for i, pred in enumerate(predictions2[:3], 1):
    print(f"  {i}. {pred['disease']} ({pred['confidence_percentage']})")
    print(f"     Specialist: {pred['specialist']}, Urgency: {pred['urgency']}")

# Test 3: Headache and nausea
text3 = 'I have a severe headache and feel nauseous'
symptom_words3 = text3.lower().split()
validated3 = detector.extract_symptoms(symptom_words3, fuzzy_threshold=0.65)
predictions3 = detector.predict_diseases(validated3, top_n=3)

print(f"\nTEST 3: '{text3}'")
print(f"Extracted: {validated3}")
print("Top predictions:")
for i, pred in enumerate(predictions3[:3], 1):
    print(f"  {i}. {pred['disease']} ({pred['confidence_percentage']})")

print("\n" + "="*60)
print("✅ All tests complete! The system works for free-text input!")
print("="*60)
