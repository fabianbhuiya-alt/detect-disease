"""
Dataset Analysis & Quality Check Script
Helps identify issues with current dataset and recommend improvements
"""

import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def analyze_dataset():
    print("="*70)
    print("DATASET ANALYSIS & QUALITY REPORT")
    print("="*70)
    
    # Load dataset
    df = pd.read_csv('ML/Diseases_and_Symptoms_dataset.csv')
    print(f"\n✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # 1. CLASS DISTRIBUTION ANALYSIS
    print("\n" + "="*70)
    print("1. CLASS DISTRIBUTION ANALYSIS")
    print("="*70)
    
    disease_counts = df['diseases'].value_counts()
    print(f"\nTotal unique diseases: {len(disease_counts)}")
    print(f"Min samples per disease: {disease_counts.min()}")
    print(f"Max samples per disease: {disease_counts.max()}")
    print(f"Mean samples per disease: {disease_counts.mean():.2f}")
    print(f"Median samples per disease: {disease_counts.median():.2f}")
    
    # Check for severe imbalance
    imbalance_ratio = disease_counts.max() / disease_counts.min()
    print(f"\n⚠ Imbalance Ratio: {imbalance_ratio:.2f}x")
    if imbalance_ratio > 10:
        print("   ❌ SEVERE CLASS IMBALANCE DETECTED!")
        print("   This significantly reduces model accuracy for minority classes")
    elif imbalance_ratio > 5:
        print("   ⚠ MODERATE CLASS IMBALANCE - May affect accuracy")
    else:
        print("   ✓ Acceptable class balance")
    
    # Top and bottom diseases
    print(f"\nTop 5 diseases by sample count:")
    for disease, count in disease_counts.head(5).items():
        print(f"  • {disease}: {count} samples ({count/len(df)*100:.1f}%)")
    
    print(f"\nBottom 5 diseases (rarest):")
    for disease, count in disease_counts.tail(5).items():
        print(f"  • {disease}: {count} samples ({count/len(df)*100:.1f}%)")
    
    # 2. SYMPTOM QUALITY ANALYSIS
    print("\n" + "="*70)
    print("2. SYMPTOM QUALITY ANALYSIS")
    print("="*70)
    
    # Get symptom columns (all except 'diseases')
    symptom_cols = [col for col in df.columns if col != 'diseases']
    
    # Count non-null values
    symptom_data = df[symptom_cols]
    print(f"\nTotal symptom features: {len(symptom_cols)}")
    
    # Check for sparsity
    non_null_counts = symptom_data.count()
    sparsity = (len(df) - non_null_counts) / len(df)
    avg_sparsity = sparsity.mean()
    
    print(f"Average feature sparsity: {avg_sparsity*100:.2f}%")
    print(f"Median symptoms per record: {(symptom_data.notna().sum(axis=1)).median():.0f}")
    print(f"Mean symptoms per record: {(symptom_data.notna().sum(axis=1)).mean():.2f}")
    
    # Check for empty rows
    empty_rows = (symptom_data.notna().sum(axis=1) == 0).sum()
    if empty_rows > 0:
        print(f"\n⚠ WARNING: {empty_rows} rows with NO symptoms!")
    
    # 3. MISSING DATA ANALYSIS
    print("\n" + "="*70)
    print("3. MISSING DATA ANALYSIS")
    print("="*70)
    
    missing_per_feature = symptom_data.isnull().sum()
    features_with_missing = (missing_per_feature > 0).sum()
    print(f"\nFeatures with missing values: {features_with_missing}/{len(symptom_cols)}")
    
    if features_with_missing > 0:
        print(f"\nTop 10 features with most missing data:")
        for feat, count in missing_per_feature.nlargest(10).items():
            pct = count/len(df)*100
            print(f"  • {feat}: {count} missing ({pct:.1f}%)")
    
    # 4. DATA TYPE & VALUE ANALYSIS
    print("\n" + "="*70)
    print("4. DATA TYPE & VALUE ANALYSIS")
    print("="*70)
    
    # Check unique values in symptoms
    print(f"\nChecking data consistency...")
    unique_vals = {}
    for col in symptom_cols[:10]:  # Check first 10
        unique_vals[col] = df[col].dropna().unique()
    
    # Look for non-binary values
    non_binary_features = []
    for col in symptom_cols:
        unique = df[col].dropna().unique()
        if len(unique) > 2:
            non_binary_features.append((col, len(unique)))
    
    if non_binary_features:
        print(f"\n⚠ Non-binary features detected: {len(non_binary_features)}")
        print("  (Expected binary: 0/1 or Yes/No)")
    else:
        print(f"\n✓ All features are properly binary")
    
    # 5. RECOMMENDATIONS
    print("\n" + "="*70)
    print("5. RECOMMENDATIONS FOR IMPROVEMENT")
    print("="*70)
    
    recommendations = []
    
    if imbalance_ratio > 10:
        recommendations.append(
            "🔴 CRITICAL: Use stratified sampling or SMOTE to balance classes\n"
            "   Command: python balance_dataset.py"
        )
    
    if avg_sparsity > 0.5:
        recommendations.append(
            "🟡 HIGH SPARSITY: Consider feature selection or dimensionality reduction\n"
            "   Many features are missing for many records"
        )
    
    if empty_rows > 0:
        recommendations.append(
            f"🟡 Remove or augment {empty_rows} empty records\n"
            "   These rows have no symptoms and confuse the model"
        )
    
    if len(non_binary_features) > 5:
        recommendations.append(
            f"🟡 Data inconsistency: {len(non_binary_features)} features aren't binary\n"
            "   Standardize all features to 0/1 format"
        )
    
    if not recommendations:
        recommendations.append("✅ Dataset looks reasonably clean!")
    
    for rec in recommendations:
        print(f"\n{rec}")
    
    # 6. QUICK IMPROVEMENT SCRIPT SUGGESTIONS
    print("\n" + "="*70)
    print("6. NEXT STEPS")
    print("="*70)
    print("""
✓ Option 1: Use publicly available medical dataset (Kaggle)
  - Better balanced, higher quality
  - Easy integration with existing code
  
✓ Option 2: Augment current dataset
  - Balance minority classes using SMOTE
  - Remove/clean problematic records
  
✓ Option 3: Retrain model with better hyperparameters
  - Use class_weight='balanced' in classifier
  - Try different algorithms (XGBoost, LightGBM)
  - Use cross-validation for better accuracy estimates
    """)
    
    return df, disease_counts

if __name__ == "__main__":
    df, disease_counts = analyze_dataset()
    
    # Save report
    print("\n" + "="*70)
    print("Saving detailed report...")
    print("="*70)
