# Free-Text Disease Prediction - How to Use

## 🎯 What Changed

Your `/search_predict` endpoint **now automatically uses the CSV detector** when the ML model isn't loaded. No more errors!

## How It Works

### Option 1: Web Interface (Easiest)

1. Start the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser to: **`http://localhost:5000/symptom_checker`**

3. Type your symptoms in natural language:
   ```
   "I have a fever, cough, and sore throat"
   ```

4. Click **"Get Predictions"** 

5. See the results with:
   - Detected symptoms
   - Top disease predictions
   - Specialist recommendations
   - Urgency levels
   - Precautions

### Option 2: API (For Developers)

**Using the `/search_predict` endpoint:**

```bash
curl -X POST http://localhost:5000/search_predict \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I have chest pain and shortness of breath",
    "fuzzy_threshold": 0.65
  }'
```

**Response:**
```json
{
  "success": true,
  "source": "CSV Dataset",
  "input_text": "I have chest pain and shortness of breath",
  "detected_symptoms": ["chest pain", "shortness of breath"],
  "predictions": [
    {
      "disease": "Coronary Artery Disease",
      "confidence": 0.95,
      "confidence_percentage": "95%",
      "specialist": "Cardiologist",
      "urgency": "High",
      "precautions": ["Healthy diet", "exercise", "statins", "avoid smoking"]
    }
  ]
}
```

**Or use the CSV endpoint directly:**

```bash
curl -X POST http://localhost:5000/api/csv/search_predict \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I have fever and cough",
    "top_n": 3
  }'
```

## Example Predictions

### Input 1: "I have a fever, cough, and sore throat"
```
Top Predictions:
1. Influenza (60%)
   - Specialist: General Practitioner
   - Urgency: Medium
   - Precautions: Rest, hydration, antivirals if severe

2. Mononucleosis (35%)
   - Specialist: General Practitioner
   - Urgency: Low
```

### Input 2: "I have chest pain and shortness of breath"
```
Top Predictions:
1. Coronary Artery Disease (HIGH CONFIDENCE)
   - Specialist: Cardiologist
   - Urgency: HIGH
   
2. Pulmonary Embolism (HIGH CONFIDENCE)
   - Specialist: Emergency Physician
   - Urgency: HIGH
```

### Input 3: "I have severe headache and feel nauseous with light sensitivity"
```
Top Predictions:
1. Migraine (HIGH CONFIDENCE)
   - Specialist: Neurologist
   - Urgency: Medium
```

## Key Features

✅ **Natural Language Understanding** - Describe symptoms however you like
✅ **Smart Fuzzy Matching** - Misspelled symptoms? No problem!
✅ **Full Disease Information** - Get specialist, urgency, and precautions
✅ **Works Without ML Models** - Uses CSV dataset automatically
✅ **Auto-Switching** - Uses ML model if available, falls back to CSV if not
✅ **Beautiful UI** - Easy-to-use web interface

## API Parameters

### `/search_predict` - Free Text Prediction
```json
{
  "text": "string - your symptom description (required)",
  "fuzzy_threshold": 0.65 // number - symptom matching strictness (optional, 0-1)
}
```

### `/api/csv/search_predict` - CSV-based Prediction
```json
{
  "text": "string - your symptom description (required)",
  "fuzzy_threshold": 0.65, // number - symptom matching strictness (optional)
  "top_n": 5 // number - number of predictions to return (optional)
}
```

## Troubleshooting

### "No recognized symptoms found"
- Try being more specific: "I have a high fever" instead of "I feel sick"
- Use common symptom names: fever, cough, pain, nausea, etc.
- Check available symptoms: Visit `/api/csv/symptoms`

### Predictions seem wrong
- The system works best with 3+ specific symptoms
- More symptoms = more accurate predictions
- Always verify with a healthcare professional

### Connection errors
- Make sure Flask app is running: `python app.py`
- Check that you're using the correct URL: `http://localhost:5000`

## Integration with Your Own App

If you have a custom frontend:

```javascript
// Example: Call disease prediction
async function getDiseaseFromSymptoms(text) {
  const response = await fetch('/search_predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({text: text})
  });
  
  const data = await response.json();
  
  if (data.success) {
    console.log('Top disease:', data.predictions[0].disease);
    console.log('Confidence:', data.predictions[0].confidence_percentage);
    console.log('See a:', data.predictions[0].specialist);
  }
}

// Use it
getDiseaseFromSymptoms('I have a fever and cough');
```

## Performance

- **Response time**: < 500ms typically
- **Accuracy**: Depends on symptom clarity
- **Coverage**: 321 diseases, 868 symptoms

## Important Disclaimer

⚠️ **This system is for informational purposes only**

- NOT a substitute for professional medical advice
- Do not self-diagnose based on this tool
- Always consult a healthcare professional
- In emergencies, call 911

✓ Use this to:
- Understand potential conditions
- Know which specialist to consult
- Prepare questions for your doctor
- Gain health literacy

## Next Steps

1. ✅ Start the app: `python app.py`
2. ✅ Open: `http://localhost:5000/symptom_checker`
3. ✅ Try describing your symptoms
4. ✅ Get predictions!

## Available Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/symptom_checker` | GET | Beautiful UI for symptom checking |
| `/search_predict` | POST | Free-text disease prediction (auto-switching) |
| `/api/csv/search_predict` | POST | CSV-based free-text prediction |
| `/api/csv/predict` | POST | Symptom list prediction |
| `/api/csv/symptoms` | GET | List all available symptoms |
| `/api/csv/diseases` | GET | List all available diseases |

---

**The system is now fully operational!** Enjoy predicting diseases from natural language symptom descriptions. 🎉
