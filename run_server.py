#!/usr/bin/env python
"""
Start Flask app with fresh model loading
Ensures new model with 5580 symptoms is loaded
"""

import os
import sys

# Change to project directory
project_dir = r'c:\Users\fabiu\OneDrive\Desktop\project\Fabian Project'
os.chdir(project_dir)

print("=" * 70)
print("🚀 STARTING FLASK WITH 5580 SYMPTOMS MODEL")
print("=" * 70)

# Verify model files
import joblib

print("\n✓ Verifying model files...")
mlb = joblib.load('Models/symptom_binarizer.pkl')
le = joblib.load('Models/disease_encoder.pkl')
model = joblib.load('Models/best_model.pkl')

print(f"  ✓ Symptoms loaded: {len(mlb.classes_)}")
print(f"  ✓ Diseases loaded: {len(le.classes_)}")
print(f"  ✓ Model ready")

print("\n" + "=" * 70)
print("Starting Flask server...")
print("=" * 70)
print("\n🌐 Visit: http://127.0.0.1:5000")
print("⚠️  Press Ctrl+C to stop\n")

# Import and run Flask app
from app import app

app.run(debug=True, port=5000)
