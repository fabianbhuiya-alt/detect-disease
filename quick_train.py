import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("=" * 70)
print("TRAINING MODEL WITH 5580 SYMPTOMS")
print("=" * 70)

# Load expanded dataset
print("\n1. Loading expanded dataset with 5580 symptoms...")
df = pd.read_csv('Data/dataset_expanded.csv')
print(f"   ✓ Loaded: {df.shape}")

# Extract symptoms (60 columns)
symptom_cols = [f'Symptom_{i}' for i in range(1, 61)]
diseases = df['Disease'].tolist()

# Create records with symptoms
print("\n2. Preparing data...")
records = []
for idx, row in df.iterrows():
    symptoms = [row[col] for col in symptom_cols if pd.notna(row[col])]
    records.append({
        'disease': row['Disease'],
        'symptoms': symptoms
    })

# Create feature matrix
print("\n3. Creating feature matrix...")
mlb = MultiLabelBinarizer()
X = mlb.fit_transform([r['symptoms'] for r in records])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform([r['disease'] for r in records])

print(f"   ✓ Feature matrix: {X.shape}")
print(f"   ✓ Total unique symptoms: {len(mlb.classes_)}")
print(f"   ✓ Total diseases: {len(le.classes_)}")

# Split data
print("\n4. Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
print("\n5. Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
print("\n6. Training Random Forest classifier...")
print("   (This may take a minute...)")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    random_state=42,
    n_jobs=-1,
    verbose=1
)
model.fit(X_train_scaled, y_train)

# Evaluate
train_acc = model.score(X_train_scaled, y_train)
test_acc = model.score(X_test_scaled, y_test)

print(f"\n7. Model Performance:")
print(f"   Train Accuracy: {train_acc:.4f}")
print(f"   Test Accuracy: {test_acc:.4f}")

# Save all models
print("\n8. Saving models...")
os.makedirs('Models', exist_ok=True)

joblib.dump(model, 'Models/best_model.pkl')
joblib.dump(mlb, 'Models/symptom_binarizer.pkl')
joblib.dump(le, 'Models/disease_encoder.pkl')
joblib.dump(scaler, 'Models/feature_scaler.pkl')

print("   ✓ best_model.pkl")
print("   ✓ symptom_binarizer.pkl")
print("   ✓ disease_encoder.pkl")
print("   ✓ feature_scaler.pkl")

# Save symptoms list
print("\n9. Saving symptoms list...")
with open('Models/all_symptoms.txt', 'w') as f:
    for symptom in sorted(mlb.classes_):
        f.write(f"{symptom}\n")

print(f"   ✓ all_symptoms.txt ({len(mlb.classes_)} symptoms)")

# Final verification
print("\n" + "=" * 70)
print("VERIFICATION")
print("=" * 70)

mlb_check = joblib.load('Models/symptom_binarizer.pkl')
le_check = joblib.load('Models/disease_encoder.pkl')

print(f"\n✓ Total symptoms in saved model: {len(mlb_check.classes_)}")
print(f"✓ Total diseases: {len(le_check.classes_)}")

print("\n✅ MODEL TRAINING COMPLETE!")
print("=" * 70)
