"""
Quick test script to verify the model and system are working
Run this after preprocessing and training
"""

import numpy as np
import pandas as pd
import joblib

print("="*60)
print("DISEASE PREDICTION SYSTEM - TEST SCRIPT")
print("="*60)

try:
    # Load all components
    print("\n1. Loading model components...")
    model = joblib.load('Models/best_model.pkl')
    le = joblib.load('Models/disease_encoder.pkl')
    scaler = joblib.load('Models/scaler.pkl')
    all_symptoms = joblib.load('Models/symptom_names.pkl')
    
    print(f"   ✓ Model loaded")
    print(f"   ✓ Disease encoder loaded ({len(le.classes_)} diseases)")
    print(f"   ✓ Scaler loaded")
    print(f"   ✓ Symptoms loaded ({len(all_symptoms)} symptoms)")
    
    # Load test data
    print("\n2. Loading test data...")
    X_test = np.load('Data/processed/X_test.npy')
    y_test = np.load('Data/processed/y_test.npy')
    print(f"   ✓ Test set: {X_test.shape[0]} samples, {X_test.shape[1]} features")
    
    # Make predictions
    print("\n3. Making predictions on test set...")
    y_pred = model.predict(X_test)
    
    from sklearn.metrics import accuracy_score, f1_score
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    print(f"   ✓ Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"   ✓ F1 Score: {f1:.4f}")
    
    # Test with sample symptoms
    print("\n4. Testing with sample input...")
    
    # Create a random feature vector (random symptoms)
    sample_features = np.random.randint(0, 2, size=len(all_symptoms))
    sample_features_scaled = scaler.transform([sample_features.astype(float)])
    
    pred_class = model.predict(sample_features_scaled)[0]
    disease = le.inverse_transform([pred_class])[0]
    
    if hasattr(model, 'predict_proba'):
        probs = model.predict_proba(sample_features_scaled)[0]
        confidence = probs[pred_class]
        print(f"   Predicted Disease: {disease}")
        print(f"   Confidence: {confidence:.4f} ({confidence*100:.2f}%)")
    
    # Test specialist recommendation
    print("\n5. Testing specialist recommendation...")
    from disease_specialist_mapping import get_specialist_for_disease
    specialists = get_specialist_for_disease(disease)
    print(f"   Recommended Specialists: {', '.join(specialists)}")
    
    print("\n" + "="*60)
    print("✓ ALL TESTS PASSED!")
    print("="*60)
    print(f"\nSystem is ready to use!")
    print(f"Run: python app_new.py")
    print(f"Then visit: http://localhost:5000")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    print("\n⚠️  Please make sure you have:")
    print("   1. Run 01_Preprocess_New_Dataset.ipynb")
    print("   2. Run 02_Train_Model.ipynb")
    print("   3. All model files are saved in Models/ folder")
