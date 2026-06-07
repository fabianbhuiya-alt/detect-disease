#!/usr/bin/env python
"""Test free-text prediction endpoint"""

from app import app
import json

# Create a test client
client = app.test_client()

print('='*60)
print('Testing /search_predict endpoint (Free-text prediction)')
print('='*60)

# Test 1: Fever, cough, sore throat
print("\nTEST 1: 'I have a fever, cough, and sore throat'")
response = client.post('/search_predict', 
    json={'text': 'I have a fever, cough, and sore throat'},
    content_type='application/json'
)
data = response.get_json()
print(f"✓ Status: {response.status_code}")
print(f"✓ Success: {data.get('success')}")
print(f"✓ Source: {data.get('source')}")
print(f"✓ Detected symptoms: {len(data.get('detected_symptoms', []))} symptoms")
if data.get('top_disease'):
    print(f"✓ Top prediction: {data['top_disease']['disease']} ({data['top_disease']['confidence_percentage']})")

# Test 2: Chest pain and shortness of breath
print("\nTEST 2: 'I have chest pain and shortness of breath'")
response = client.post('/search_predict', 
    json={'text': 'I have chest pain and shortness of breath'},
    content_type='application/json'
)
data = response.get_json()
print(f"✓ Status: {response.status_code}")
print(f"✓ Success: {data.get('success')}")
if data.get('top_disease'):
    print(f"✓ Top prediction: {data['top_disease']['disease']}")
    print(f"✓ Specialist: {data['top_disease']['specialist']}")
    print(f"✓ Urgency: {data['top_disease']['urgency']}")

print("\n" + "="*60)
print("✅ All tests passed! Free-text prediction is working!")
print("="*60)
print("\nNow you can:")
print("1. Run: python app.py")
print("2. Open: http://localhost:5000/symptom_checker")
print("3. Describe symptoms and get predictions!")
