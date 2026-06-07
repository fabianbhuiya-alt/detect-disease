import pandas as pd
import os

print("=" * 60)
print("SYMPTOM COUNT ANALYSIS")
print("=" * 60)

# Check original dataset
print("\n1. ORIGINAL DATASET:")
if os.path.exists('Data/dataset.csv'):
    df_orig = pd.read_csv('Data/dataset.csv')
    print(f"   Rows: {df_orig.shape[0]}")
    print(f"   Symptom columns: {df_orig.shape[1] - 1}")
    
    symptoms_orig = set()
    for i in range(1, 18):
        col = f'Symptom_{i}'
        symptoms_orig.update(df_orig[col].dropna().unique())
    
    print(f"   ✓ TOTAL UNIQUE SYMPTOMS: {len(symptoms_orig)}")
else:
    print("   ✗ Not found")

# Check expanded dataset
print("\n2. EXPANDED DATASET:")
if os.path.exists('Data/dataset_expanded.csv'):
    df_exp = pd.read_csv('Data/dataset_expanded.csv')
    print(f"   Rows: {df_exp.shape[0]}")
    print(f"   Symptom columns: {df_exp.shape[1] - 1}")
    
    symptoms_exp = set()
    for col in df_exp.columns:
        if col.startswith('Symptom_'):
            symptoms_exp.update(df_exp[col].dropna().unique())
    
    print(f"   ✓ TOTAL UNIQUE SYMPTOMS: {len(symptoms_exp)}")
else:
    print("   ✗ Not found")

print("\n" + "=" * 60)
