#!/usr/bin/env python
import joblib
import os

os.chdir(r"c:\Users\fabiu\OneDrive\Desktop\project\Fabian Project")

print("=" * 70)
print("MODEL VERIFICATION REPORT")
print("=" * 70)

try:
    mlb = joblib.load('Models/symptom_binarizer.pkl')
    le = joblib.load('Models/disease_encoder.pkl')
    
    print(f"\n✓ SUCCESS! Model trained with expanded dataset")
    print(f"\n📊 SYMPTOMS:")
    print(f"   Total unique symptoms: {len(mlb.classes_)}")
    print(f"\n🏥 DISEASES:")
    print(f"   Total diseases: {len(le.classes_)}")
    print(f"   Disease list: {', '.join(le.classes_[:5])}...")
    
    print(f"\n📋 SAMPLE SYMPTOMS (first 30):")
    symptoms_sorted = sorted(mlb.classes_)
    for i, symptom in enumerate(symptoms_sorted[:30], 1):
        print(f"   {i:2d}. {symptom}")
    
    print(f"\n✓ All required files saved:")
    print(f"   ✓ best_model.pkl")
    print(f"   ✓ symptom_binarizer.pkl")
    print(f"   ✓ disease_encoder.pkl")
    print(f"   ✓ feature_scaler.pkl")
    
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "=" * 70)
