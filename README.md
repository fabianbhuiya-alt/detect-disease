# 🏥 Disease Prediction System with Specialist Recommendation

A complete machine learning system that predicts diseases based on patient symptoms and recommends appropriate medical specialists.

## 📊 Features

- ✅ **Symptom-based disease prediction** using your dataset with 50K+ syndromes
- ✅ **High accuracy models** (Random Forest, Gradient Boosting, XGBoost, SVM)
- ✅ **Specialist recommendations** based on predicted disease
- ✅ **Confidence scores** showing prediction reliability
- ✅ **Top 5 predictions** with probabilities
- ✅ **User-friendly web interface** for easy symptom selection
- ✅ **REST API** for integration with other systems

## 📁 Project Structure

```
project/
├── ML/
│   ├── Diseases_and_Symptoms_dataset.csv    # Your dataset
│   ├── 01_Preprocess_New_Dataset.ipynb      # Data preprocessing
│   ├── 02_Train_Model.ipynb                 # Model training
│   └── [Other notebooks]
├── Data/
│   ├── dataset.csv                          # Original dataset
│   └── processed/                           # Preprocessed data (created)
│       ├── X_train.npy
│       ├── X_test.npy
│       ├── y_train.npy
│       └── y_test.npy
├── Models/                                  # Saved models (created)
│   ├── best_model.pkl
│   ├── disease_encoder.pkl
│   ├── scaler.pkl
│   └── symptom_names.pkl
├── templates/
│   └── index.html                           # Web interface
├── static/
│   └── style.css
├── app_new.py                               # Flask application
├── disease_specialist_mapping.py            # Disease-specialist mapping
├── test_system.py                           # System test script
└── requirements.txt
```

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Preprocess the Data

Open the Jupyter notebook and run all cells:

```
ML/01_Preprocess_New_Dataset.ipynb
```

This will:
- Load your `Diseases_and_Symptoms_dataset.csv`
- Clean and normalize the data
- Create train/test splits
- Save preprocessed data to `Data/processed/`
- Save encoders and scalers to `Models/`

**Expected output:**
```
✓ Dataset shape: (your_samples, features)
✓ All files saved successfully!
  - X_train.npy, X_test.npy, y_train.npy, y_test.npy
  - disease_encoder.pkl
  - scaler.pkl
  - symptom_names.pkl
```

### Step 3: Train the Model

Open the Jupyter notebook and run all cells:

```
ML/02_Train_Model.ipynb
```

This will:
- Train multiple models (Random Forest, Gradient Boosting, XGBoost, SVM)
- Compare their accuracy
- Save the best model to `Models/best_model.pkl`

**Expected output:**
```
==================================================
SUMMARY
==================================================
                Model  Train Accuracy  Test Accuracy  F1 Score
0        Random Forest            0.95           0.87       0.86
1   Gradient Boosting            0.94           0.88       0.87
2            XGBoost            0.93           0.86       0.85
3                SVM            0.91           0.84       0.83

✓ Best Model: Gradient Boosting with 0.88 accuracy
```

### Step 4: Test the System

Run the test script to verify everything is working:

```bash
python test_system.py
```

**Expected output:**
```
============================================================
DISEASE PREDICTION SYSTEM - TEST SCRIPT
============================================================

1. Loading model components...
   ✓ Model loaded
   ✓ Disease encoder loaded (X diseases)
   ✓ Scaler loaded
   ✓ Symptoms loaded (Y symptoms)

2. Loading test data...
   ✓ Test set: Z samples, Y features

3. Making predictions on test set...
   ✓ Accuracy: 0.88 (88.00%)
   ✓ F1 Score: 0.87

4. Testing with sample input...
   Predicted Disease: [disease_name]
   Confidence: 0.92 (92.34%)

5. Testing specialist recommendation...
   Recommended Specialists: [specialist1], [specialist2]

============================================================
✓ ALL TESTS PASSED!
============================================================
```

### Step 5: Run the Web Application

Start the Flask server:

```bash
python app_new.py
```

Open your browser and go to: **http://localhost:5000**

You'll see:
- List of all symptoms
- Checkboxes to select symptoms
- "Predict Disease" button
- Results showing:
  - Predicted disease
  - Confidence percentage
  - Recommended specialists
  - Top 5 possible diseases

## 📡 API Endpoints

### GET /api/symptoms
Get list of all available symptoms

**Response:**
```json
{
    "symptoms": ["anxiety and nervousness", "depression", ...],
    "total": 131
}
```

### GET /api/diseases
Get list of all available diseases

**Response:**
```json
{
    "diseases": ["panic disorder", "disease2", ...],
    "total": 120
}
```

### POST /predict
Predict disease based on symptoms

**Request:**
```json
{
    "symptoms": {
        "anxiety and nervousness": 1,
        "depression": 0,
        "shortness of breath": 1,
        ...
    }
}
```

**Response:**
```json
{
    "success": true,
    "predicted_disease": "panic disorder",
    "confidence": 0.92,
    "confidence_percentage": "92.34%",
    "recommended_specialists": ["Psychiatrist", "Clinical Psychologist"],
    "top_predictions": [
        {"disease": "panic disorder", "probability": 0.92},
        {"disease": "anxiety", "probability": 0.05},
        ...
    ],
    "symptoms_reported": 15,
    "total_symptoms_available": 131
}
```

## 📈 Model Performance

The system is trained on your dataset with:
- **131 symptoms** from your dataset
- **Multiple disease classes**
- **Data preprocessing** including normalization and scaling
- **Multiple algorithms** compared for best performance
- **Class balancing** to handle imbalanced data

**Expected Accuracy:** 80-90% depending on your dataset quality

## 🔄 Workflow

1. **Data Preprocessing** → Normalizes and scales symptoms
2. **Feature Engineering** → Converts symptoms to binary features
3. **Model Training** → Trains multiple models and selects best
4. **Disease Prediction** → Predicts disease from symptom patterns
5. **Specialist Mapping** → Recommends appropriate specialists
6. **Confidence Scoring** → Shows prediction reliability

## 🎯 Disease-Specialist Mapping

The system automatically recommends specialists based on disease:

Examples:
- `Panic Disorder` → Psychiatrist, Neurologist, Clinical Psychologist
- `Diabetes` → Endocrinologist, Internal Medicine
- `Pneumonia` → Pulmonologist, Infectious Disease
- `Hypertension` → Cardiologist, Internal Medicine

See `disease_specialist_mapping.py` for the complete mapping.

## ⚠️ Troubleshooting

### Models not found error
```
❌ ERROR: No such file or directory: 'Models/best_model.pkl'
```
**Solution:** Run the preprocessing and training notebooks first!

### Not enough data error
```
❌ ValueError: n_splits=5 greater than the number of samples
```
**Solution:** Your dataset might be too small. Increase dataset size or reduce n_splits.

### Memory error during training
```
MemoryError: Unable to allocate memory
```
**Solution:** 
- Reduce model parameters
- Use a smaller test size
- Run on a machine with more RAM

## 📝 Requirements

```
numpy<2.0
pandas
scipy
scikit-learn
xgboost
imbalanced-learn
joblib
flask
flask-cors
ipykernel
```

## 🔐 Disclaimer

This system is for **educational and demonstration purposes**. For actual medical diagnosis:
- Always consult with qualified medical professionals
- Use this as a **supplementary tool only**
- Do not replace professional medical advice
- Verify predictions with clinical assessments

## 📧 Support

If you encounter issues:
1. Check the test_system.py output
2. Verify all required files are in the correct directories
3. Ensure all dependencies are installed
4. Check Flask server logs for API errors

## 📚 References

- Dataset: Your `Diseases_and_Symptoms_dataset.csv`
- Symptoms: 131 distinct symptoms
- Diseases: Multiple disease categories
- Models: Scikit-learn, XGBoost

---

**Happy Diagnosing! 🏥**
# detect-disease
