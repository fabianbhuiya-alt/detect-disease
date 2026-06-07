"""
Simple improved training script without unicode issues
Trains on the public medical dataset quickly
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

def train_simple_model():
    """Train a simple but effective model"""
    
    print("="*70)
    print("TRAINING IMPROVED MODEL - PUBLIC MEDICAL DATASET")
    print("="*70)
    
    # Load dataset
    print("\n[1] Loading public medical dataset...")
    df = pd.read_csv('ML/public_medical_dataset.csv')
    
    print(f"    Records: {len(df)}")
    print(f"    Features: {len(df.columns)-1}")
    print(f"    Diseases: {df['disease'].nunique()}")
    
    # Separate features and target
    X = df.drop('disease', axis=1).astype(float)
    y = df['disease']
    
    # Split data
    print("\n[2] Splitting data (80/20)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    print("[3] Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"    Train set: {X_train.shape}")
    print(f"    Test set: {X_test.shape}")
    
    # Train model
    print("\n[4] Training Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        max_features='sqrt',
        random_state=42,
        n_jobs=-1,
        class_weight='balanced'
    )
    
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    print("[5] Evaluating model...")
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    print("\n" + "="*70)
    print("MODEL PERFORMANCE - PUBLIC MEDICAL DATASET")
    print("="*70)
    print(f"\n  Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall:    {recall:.4f}")
    print(f"  F1 Score:  {f1:.4f}")
    
    # Save model
    print("\n[6] Saving model...")
    joblib.dump(model, 'Models/best_model_public.pkl')
    joblib.dump(scaler, 'Models/scaler_public.pkl')
    
    print("    Saved: Models/best_model_public.pkl")
    print("    Saved: Models/scaler_public.pkl")
    
    # Also train on enhanced dataset
    print("\n" + "="*70)
    print("TRAINING ON ENHANCED MEDICAL DATASET")
    print("="*70)
    
    print("\n[1] Loading enhanced medical dataset...")
    df2 = pd.read_csv('ML/enhanced_medical_dataset.csv')
    
    print(f"    Records: {len(df2)}")
    print(f"    Features: {len(df2.columns)-1}")
    print(f"    Diseases: {df2['disease'].nunique()}")
    
    # Prepare data
    X2 = df2.drop('disease', axis=1).astype(float)
    y2 = df2['disease']
    
    print("\n[2] Splitting data (80/20)...")
    X_train2, X_test2, y_train2, y_test2 = train_test_split(
        X2, y2, test_size=0.2, random_state=42, stratify=y2
    )
    
    print("[3] Scaling features...")
    scaler2 = StandardScaler()
    X_train2_scaled = scaler2.fit_transform(X_train2)
    X_test2_scaled = scaler2.transform(X_test2)
    
    print(f"    Train set: {X_train2.shape}")
    print(f"    Test set: {X_test2.shape}")
    
    print("\n[4] Training Random Forest Classifier...")
    model2 = RandomForestClassifier(
        n_estimators=150,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        max_features='sqrt',
        random_state=42,
        n_jobs=-1,
        class_weight='balanced'
    )
    
    model2.fit(X_train2_scaled, y_train2)
    
    print("[5] Evaluating model...")
    y_pred2 = model2.predict(X_test2_scaled)
    
    accuracy2 = accuracy_score(y_test2, y_pred2)
    precision2 = precision_score(y_test2, y_pred2, average='weighted', zero_division=0)
    recall2 = recall_score(y_test2, y_pred2, average='weighted', zero_division=0)
    f1_2 = f1_score(y_test2, y_pred2, average='weighted', zero_division=0)
    
    print("\n" + "="*70)
    print("MODEL PERFORMANCE - ENHANCED MEDICAL DATASET")
    print("="*70)
    print(f"\n  Accuracy:  {accuracy2:.4f} ({accuracy2*100:.2f}%)")
    print(f"  Precision: {precision2:.4f}")
    print(f"  Recall:    {recall2:.4f}")
    print(f"  F1 Score:  {f1_2:.4f}")
    
    print("\n[6] Saving model...")
    joblib.dump(model2, 'Models/best_model_enhanced.pkl')
    joblib.dump(scaler2, 'Models/scaler_enhanced.pkl')
    
    print("    Saved: Models/best_model_enhanced.pkl")
    print("    Saved: Models/scaler_enhanced.pkl")
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY - MODEL COMPARISON")
    print("="*70)
    
    print(f"\nPublic Medical Dataset Model:")
    print(f"  Accuracy:  {accuracy*100:.2f}%")
    
    print(f"\nEnhanced Medical Dataset Model:")
    print(f"  Accuracy:  {accuracy2*100:.2f}%")
    
    if accuracy2 > accuracy:
        print(f"\nBEST MODEL: Enhanced Dataset ({accuracy2*100:.2f}%)")
        print("Using: Models/best_model_enhanced.pkl")
    else:
        print(f"\nBEST MODEL: Public Dataset ({accuracy*100:.2f}%)")
        print("Using: Models/best_model_public.pkl")
    
    print("\n" + "="*70)
    print("NEXT STEPS:")
    print("="*70)
    print("""
1. Update your app.py to use the new model:
   
   OLD:
   model = joblib.load('Models/best_model.pkl')
   scaler = joblib.load('Models/scaler.pkl')
   
   NEW:
   model = joblib.load('Models/best_model_enhanced.pkl')
   scaler = joblib.load('Models/scaler_enhanced.pkl')

2. Test your system:
   python test_system.py

3. Compare accuracy improvement:
   Check if predictions are now more accurate!
""")

if __name__ == "__main__":
    train_simple_model()
