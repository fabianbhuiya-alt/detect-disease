"""
Generate model files from the disease-symptoms CSV data
This creates the pickle files needed by app.py
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
import pickle

print("=" * 60)
print("GENERATING MODEL FILES")
print("=" * 60)

# Create Models directory if it doesn't exist
os.makedirs('Models', exist_ok=True)

# Load the disease-symptoms CSV
print("\n1. Loading CSV data...")
csv_path = 'disease-symptoms-precautions-specialist.csv'
df = pd.read_csv(csv_path)
print(f"   ✓ Loaded {len(df)} rows with columns: {df.columns.tolist()}")

# Extract symptoms column
print("\n2. Extracting symptoms...")
if 'Symptom' in df.columns or 'symptoms' in df.columns:
    symptom_col = 'Symptom' if 'Symptom' in df.columns else 'symptoms'
else:
    symptom_col = df.columns[1]  # Use second column

if 'Disease' in df.columns or 'disease' in df.columns:
    disease_col = 'Disease' if 'Disease' in df.columns else 'disease'
else:
    disease_col = df.columns[0]  # Use first column

print(f"   Using columns: {disease_col} -> {symptom_col}")

# Create symptom list
symptoms = df[symptom_col].unique()
all_symptoms = sorted([str(s).strip().lower() for s in symptoms if pd.notna(s)])
diseases = df[disease_col].unique()

print(f"   ✓ Found {len(all_symptoms)} unique symptoms")
print(f"   ✓ Found {len(diseases)} unique diseases")

# Save symptoms list
print("\n3. Saving symptoms list...")
with open('Models/all_symptoms.txt', 'w') as f:
    for symptom in all_symptoms:
        f.write(symptom + '\n')
print(f"   ✓ Saved to Models/all_symptoms.txt")

# Create feature matrix from symptoms (one-hot encoding for symptoms)
print("\n4. Creating feature matrix...")
symptom_to_idx = {s: i for i, s in enumerate(all_symptoms)}

X = np.zeros((len(df), len(all_symptoms)))
for idx, row in df.iterrows():
    symp = str(row[symptom_col]).strip().lower()
    if symp in symptom_to_idx:
        X[idx, symptom_to_idx[symp]] = 1

# Encode diseases
print("\n5. Encoding disease labels...")
le = LabelEncoder()
y = le.fit_transform(df[disease_col])
print(f"   ✓ {len(le.classes_)} disease classes")

# Save label encoder
print("\n6. Saving label encoder...")
joblib.dump(le, 'Models/disease_encoder.pkl')
print(f"   ✓ Saved to Models/disease_encoder.pkl")

# Scale features
print("\n7. Creating scaler...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, 'Models/scaler.pkl')
print(f"   ✓ Saved to Models/scaler.pkl")

# Train a simple model
print("\n8. Training Random Forest model...")
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Get accuracy
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"   Train accuracy: {train_score:.2%}")
print(f"   Test accuracy: {test_score:.2%}")

# Save model
print("\n9. Saving trained model...")
joblib.dump(model, 'Models/disease_prediction_model.pkl')
print(f"   ✓ Saved to Models/disease_prediction_model.pkl")

# Save symptoms list as pickle too
print("\n10. Saving additional files...")
with open('Models/trained_symptoms.pkl', 'wb') as f:
    pickle.dump(all_symptoms, f)
print(f"    ✓ Saved to Models/trained_symptoms.pkl")

with open('Models/disease_classes.pkl', 'wb') as f:
    pickle.dump(le.classes_, f)
print(f"    ✓ Saved to Models/disease_classes.pkl")

print("\n" + "=" * 60)
print("✓ ALL MODEL FILES GENERATED SUCCESSFULLY!")
print("=" * 60)
print("\nGenerated files:")
print(f"  - Models/disease_encoder.pkl")
print(f"  - Models/scaler.pkl")
print(f"  - Models/disease_prediction_model.pkl")
print(f"  - Models/all_symptoms.txt")
print(f"  - Models/trained_symptoms.pkl")
print(f"  - Models/disease_classes.pkl")
print("\nYou can now run: python app.py")
print("=" * 60)
