import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def prepare_enhanced_dataset():
    """Prepare enhanced dataset with all symptoms"""
    
    # Read and clean dataset (use expanded dataset with 5580 symptoms)
    df = pd.read_csv('Data/dataset_expanded.csv')
    
    # Clean symptom names
    def clean_symptom(s):
        if pd.isna(s):
            return None
        s = str(s).strip().lower()
        # Fix specific issues
        corrections = {
            'spotting_ urination': 'spotting_urination',
            'ochromic _patches': 'dischromic_patches',
            'dischromic _patches': 'dischromic_patches',
            'yellowing_of_eyes': 'yellowing_eyes',
            'yellow_urine': 'dark_urine',
            'receiving_unsterile_injections': 'unsterile_injections',
        }
        s = corrections.get(s, s)
        s = s.replace('_ ', '_').replace(' _', '_').replace(' ', '_')
        return s if s and s != 'nan' else None
    
    symptom_cols = [f'Symptom_{i}' for i in range(1, 61)]  # Expanded to 60 columns
    for col in symptom_cols:
        df[col] = df[col].apply(clean_symptom)
    
    # Create symptom list per row
    all_records = []
    for idx, row in df.iterrows():
        disease = row['Disease'].strip()
        symptoms = [row[col] for col in symptom_cols if pd.notna(row[col])]
        if symptoms:
            all_records.append({'disease': disease, 'symptoms': list(set(symptoms))})
    
    # Get unique diseases and symptoms
    diseases = list(set([r['disease'] for r in all_records]))
    all_symptoms = list(set([s for r in all_records for s in r['symptoms']]))
    
    print(f"Total diseases: {len(diseases)}")
    print(f"Total unique symptoms: {len(all_symptoms)}")
    
    # Create feature matrix using MultiLabelBinarizer
    mlb = MultiLabelBinarizer()
    X = mlb.fit_transform([r['symptoms'] for r in all_records])
    
    # Create target labels
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform([r['disease'] for r in all_records])
    
    return X, y, mlb, le, all_symptoms, diseases

def train_models():
    """Train multiple models and select best"""
    
    X, y, mlb, le, all_symptoms, diseases = prepare_enhanced_dataset()
    
    print(f"\nFeature matrix shape: {X.shape}")
    print(f"Target classes: {len(le.classes_)}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Test different models
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=150, max_depth=5, random_state=42),
        'Random Forest (tuned)': RandomForestClassifier(
            n_estimators=300,
            max_depth=25,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42
        )
    }
    
    best_model = None
    best_accuracy = 0
    
    for name, model in models.items():
        # Cross-validation
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
        print(f"\n{name}:")
        print(f"  CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
        
        # Train and evaluate
        model.fit(X_train_scaled, y_train)
        train_acc = model.score(X_train_scaled, y_train)
        test_acc = model.score(X_test_scaled, y_test)
        print(f"  Train Accuracy: {train_acc:.4f}")
        print(f"  Test Accuracy: {test_acc:.4f}")
        
        if test_acc > best_accuracy:
            best_accuracy = test_acc
            best_model = model
    
    print(f"\nBest Model Test Accuracy: {best_accuracy:.4f}")
    
    # Save model and encoders
    joblib.dump(best_model, 'Models/best_model.pkl')
    joblib.dump(mlb, 'Models/symptom_binarizer.pkl')
    joblib.dump(le, 'Models/disease_encoder.pkl')
    joblib.dump(scaler, 'Models/feature_scaler.pkl')
    
    # Save symptoms list for frontend (from mlb.classes_ which has all 5580 symptoms)
    with open('Models/all_symptoms.txt', 'w') as f:
        for symptom in sorted(mlb.classes_):
            f.write(f"{symptom}\n")
    
    print("\n✓ Model and encoders saved successfully!")
    return best_model, mlb, le, scaler, all_symptoms

if __name__ == '__main__':
    train_models()
