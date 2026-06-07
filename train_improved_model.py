"""
OPTION 2: Retrain Current Model with Better Hyperparameters
This script improves accuracy using optimized settings and better algorithms
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import joblib
import warnings
warnings.filterwarnings('ignore')

def load_and_prepare_data(dataset_path='ML/Diseases_and_Symptoms_dataset.csv'):
    """Load and prepare data"""
    print("Loading dataset...")
    df = pd.read_csv(dataset_path)
    
    # Separate features and target
    X = df.drop('diseases', axis=1).astype(float)
    y = df['diseases']
    
    print(f"Dataset shape: {X.shape}")
    print(f"Classes: {len(y.unique())}")
    
    return X, y

def train_improved_model(X, y, model_name='xgboost'):
    """Train model with optimized hyperparameters"""
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"\nTraining set: {X_train.shape}")
    print(f"Test set: {X_test.shape}")
    
    # Train different models
    if model_name == 'xgboost':
        print("\n🚀 Training XGBoost Classifier...")
        model = XGBClassifier(
            n_estimators=200,
            max_depth=7,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            gamma=1,
            min_child_weight=1,
            reg_alpha=0.1,
            reg_lambda=1.0,
            scale_pos_weight=1,
            random_state=42,
            n_jobs=-1,
            tree_method='hist',
            device='cpu'
        )
        model.fit(X_train, y_train)
        
    elif model_name == 'gradient_boosting':
        print("\n🚀 Training Gradient Boosting Classifier...")
        model = GradientBoostingClassifier(
            n_estimators=200,
            learning_rate=0.1,
            max_depth=5,
            min_samples_split=5,
            min_samples_leaf=2,
            subsample=0.8,
            random_state=42
        )
        model.fit(X_train, y_train)
        
    elif model_name == 'random_forest':
        print("\n🚀 Training Random Forest Classifier...")
        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=20,
            min_samples_split=5,
            min_samples_leaf=2,
            max_features='sqrt',
            random_state=42,
            n_jobs=-1,
            class_weight='balanced'
        )
        model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    print(f"\n📊 Results for {model_name}:")
    print(f"  Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall:    {recall:.4f}")
    print(f"  F1 Score:  {f1:.4f}")
    
    # Cross-validation score
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(model, X_train, y_train, cv=skf, scoring='accuracy', n_jobs=-1)
    print(f"  Cross-Val: {cv_scores.mean():.4f} (±{cv_scores.std():.4f})")
    
    return model, accuracy, X_test, y_test, y_pred, scaler

def train_ensemble_model(X, y):
    """Train ensemble model combining multiple algorithms"""
    print("\n" + "="*70)
    print("TRAINING ENSEMBLE MODEL (Best Performance)")
    print("="*70)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("\n🔨 Building ensemble with 3 algorithms...")
    
    # Random Forest
    rf = RandomForestClassifier(
        n_estimators=150,
        max_depth=20,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1,
        class_weight='balanced'
    )
    
    # Gradient Boosting
    gb = GradientBoostingClassifier(
        n_estimators=150,
        learning_rate=0.1,
        max_depth=5,
        min_samples_split=5,
        random_state=42
    )
    
    # XGBoost
    xgb = XGBClassifier(
        n_estimators=150,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1
    )
    
    # Voting ensemble
    voting_clf = VotingClassifier(
        estimators=[('rf', rf), ('gb', gb), ('xgb', xgb)],
        voting='soft'
    )
    
    voting_clf.fit(X_train, y_train)
    y_pred = voting_clf.predict(X_test)
    
    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    print(f"\n📊 Ensemble Results:")
    print(f"  Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall:    {recall:.4f}")
    print(f"  F1 Score:  {f1:.4f}")
    
    # Cross-validation
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(voting_clf, X_train, y_train, cv=skf, scoring='accuracy', n_jobs=-1)
    print(f"  Cross-Val: {cv_scores.mean():.4f} (±{cv_scores.std():.4f})")
    
    return voting_clf, accuracy, X_test, y_test, y_pred, scaler

def main():
    print("="*70)
    print("IMPROVED MODEL TRAINING WITH OPTIMIZED HYPERPARAMETERS")
    print("="*70)
    
    # Load data
    X, y = load_and_prepare_data()
    
    # Train multiple models
    results = {}
    best_model = None
    best_accuracy = 0
    best_scaler = None
    best_model_name = None
    
    print("\n" + "="*70)
    print("TESTING INDIVIDUAL MODELS")
    print("="*70)
    
    for model_name in ['random_forest', 'gradient_boosting', 'xgboost']:
        try:
            model, accuracy, X_test, y_test, y_pred, scaler = train_improved_model(X, y, model_name)
            results[model_name] = accuracy
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = model
                best_scaler = scaler
                best_model_name = model_name
                best_X_test = X_test
                best_y_test = y_test
                best_y_pred = y_pred
        except Exception as e:
            print(f"❌ Error training {model_name}: {e}")
    
    # Train ensemble
    try:
        ensemble_model, ens_accuracy, X_test, y_test, y_pred, scaler = train_ensemble_model(X, y)
        results['ensemble'] = ens_accuracy
        
        if ens_accuracy > best_accuracy:
            best_accuracy = ens_accuracy
            best_model = ensemble_model
            best_scaler = scaler
            best_model_name = 'ensemble'
            best_X_test = X_test
            best_y_test = y_test
            best_y_pred = y_pred
    except Exception as e:
        print(f"❌ Error training ensemble: {e}")
    
    # Summary
    print("\n" + "="*70)
    print("MODEL COMPARISON SUMMARY")
    print("="*70)
    
    for model_name, accuracy in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f"  {model_name:20s}: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    print(f"\n🏆 BEST MODEL: {best_model_name.upper()} with {best_accuracy*100:.2f}% accuracy")
    
    # Save best model
    print("\n" + "="*70)
    print("SAVING BEST MODEL")
    print("="*70)
    
    joblib.dump(best_model, 'Models/best_model_improved.pkl')
    joblib.dump(best_scaler, 'Models/scaler_improved.pkl')
    
    print(f"✓ Model saved: Models/best_model_improved.pkl")
    print(f"✓ Scaler saved: Models/scaler_improved.pkl")
    
    # Detailed classification report
    print("\n" + "="*70)
    print("DETAILED CLASSIFICATION REPORT (Top 20 Classes)")
    print("="*70)
    
    report = classification_report(best_y_test, best_y_pred, output_dict=True)
    
    # Get top 20 by support
    classes = list(report.keys())[:-3]  # Exclude accuracy, macro avg, weighted avg
    class_supports = [(c, report[c]['support']) for c in classes]
    class_supports.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\n{'Class':<30} {'Precision':>10} {'Recall':>10} {'F1':>10} {'Support':>8}")
    print("-" * 70)
    
    for class_name, support in class_supports[:20]:
        p = report[class_name]['precision']
        r = report[class_name]['recall']
        f1 = report[class_name]['f1-score']
        print(f"{class_name:<30} {p:>10.3f} {r:>10.3f} {f1:>10.3f} {support:>8.0f}")
    
    print("\n✅ Model training complete!")

if __name__ == "__main__":
    main()
