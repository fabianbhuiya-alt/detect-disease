import joblib
import os

print("=" * 70)
print("VERIFYING MODEL TRAINING")
print("=" * 70)

if os.path.exists('Models/best_model.pkl'):
    model = joblib.load('Models/best_model.pkl')
    mlb = joblib.load('Models/symptom_binarizer.pkl')
    le = joblib.load('Models/disease_encoder.pkl')
    scaler = joblib.load('Models/feature_scaler.pkl')
    
    print(f"\n✓ Model trained successfully!")
    print(f"\nModel Details:")
    print(f"  Model type: {type(model).__name__}")
    print(f"  Number of features (symptoms): {mlb.classes_.shape[0]}")
    print(f"  Number of classes (diseases): {len(le.classes_)}")
    print(f"  Diseases: {', '.join(le.classes_[:5])}...")
    
    print(f"\nSymptom Binarizer:")
    print(f"  Total unique symptoms: {len(mlb.classes_)}")
    print(f"  Sample symptoms:")
    for symptom in sorted(mlb.classes_)[:15]:
        print(f"    - {symptom}")
    
    print(f"\n✓ All model files saved:")
    print(f"  - best_model.pkl")
    print(f"  - symptom_binarizer.pkl")
    print(f"  - disease_encoder.pkl")
    print(f"  - feature_scaler.pkl")
else:
    print("✗ Model file not found!")

print("\n" + "=" * 70)
