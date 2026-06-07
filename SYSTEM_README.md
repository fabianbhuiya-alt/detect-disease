# 🏥 AI Symptom Checker - Consumer Web App

A modern, mobile-friendly **symptom checker web application** that uses machine learning to predict diseases and recommend specialists, with **Google Maps integration** to find healthcare providers nearby.

## ✨ Features

### 1. **Smart Symptom Search**
- Type symptoms or feelings in a search box
- Real-time autocomplete suggestions
- Support for multiple symptoms
- Easy removal of selected symptoms

### 2. **AI Disease Prediction**
- Machine learning model predicts diseases from symptoms
- Shows confidence level with visual progress bar
- Displays top 5 alternative predictions
- Analyzes all selected symptoms

### 3. **Specialist Recommendations**
- Recommends the right specialist for each disease
- Shows multiple specialists if applicable
- Click any specialist to find them on the map

### 4. **🗺️ Google Maps Integration**
- Find specialists near your location
- Search by address or city
- Auto-detect current location (GPS)
- Shows markers for all nearby hospitals/clinics
- View ratings and reviews
- Get directions with one click

### 5. **Consumer-Friendly UI**
- Clean, modern design
- Works on mobile, tablet, and desktop
- Responsive layout
- Fast and easy to use
- Beautiful gradient theme

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Flask and required packages (see requirements.txt)
- Trained ML model files

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Google Maps API Key
See [GOOGLE_MAPS_SETUP.md](GOOGLE_MAPS_SETUP.md) for detailed instructions

### 3. Configure API Key
Update in `templates/index.html` (line 3):
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places"></script>
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Browser
```
http://localhost:5000
```

## 📋 How to Use

### Step 1: Describe Your Symptoms
1. Click in the search box that says "Type your symptoms..."
2. Type a symptom (e.g., "headache", "fever", "cough")
3. See suggestions appear in real-time
4. Press **Enter** or click a suggestion to add it

### Step 2: Check Your Disease
1. Add multiple symptoms for better accuracy
2. Click **🔍 Check Disease** button
3. Wait for the AI to analyze your symptoms

### Step 3: View Results
- **Predicted Disease**: Most likely disease based on symptoms
- **Confidence Level**: How confident the model is (0-100%)
- **Recommended Specialists**: Who to see for this disease
- **Alternative Conditions**: Other possible diseases

### Step 4: Find Specialists Near You
1. Click on any specialist badge to search for them
2. Or enter your city/address in the search box
3. Click **Search** to find nearby specialists
4. Map shows all hospitals/clinics with markers
5. Click markers to see details, ratings, and address

### Using Your Current Location
1. Click **Use My Location** button
2. Allow browser access to your location
3. System automatically finds nearby specialists

## 🎨 UI Components

### Left Panel: Symptom Input
- Search box with autocomplete
- Selected symptoms display as tags
- Remove button (×) on each tag
- Button to predict disease
- Help tip for users

### Right Panel: Quick Results
- Shows predicted disease
- Confidence level indicator
- Preview of results

### Bottom Section: Full Results
1. **Specialist Recommendations**: Interactive badges
2. **Google Map**: Find specialists with GPS coordinates
3. **Alternative Conditions**: All predictions ranked by probability

## 📊 Disease Prediction Accuracy

The system uses your trained ML model with:
- All available symptoms as features
- Trained disease classification model
- Probability scores for confidence
- Top 5 predictions ranked by probability

## 🗺️ Google Maps Features

### Search Capabilities
- Search within 5km radius (customizable)
- Supports multiple specialist types
- Shows up to 5 results per specialist

### Map Interactions
- **Zoom In/Out**: Use mouse wheel or +/- buttons
- **Pan**: Click and drag to move map
- **Click Marker**: See place details (name, address, rating)
- **Info Windows**: Click markers to view details

### Specialist Search Types
- Cardiologist
- Neurologist
- Dermatologist
- Psychiatrist
- And 100+ more specialists!

## 🔧 Customization

### Change Search Radius
Edit `templates/index.html` around line 525:
```javascript
radius: 5000, // 5000 meters = 5 km
```

Change to:
```javascript
radius: 10000, // 10 km
```

### Modify Default Location
Edit `templates/index.html` around line 460:
```javascript
const defaultLocation = { lat: 20.5937, lng: 78.9629 }; // India
```

### Customize UI Colors
Edit CSS variables in `templates/index.html`:
```css
/* Primary color (Purple) */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to your brand colors */
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
```

## 📱 Responsive Design

- **Desktop**: Full 2-column layout
- **Tablet**: Single column, optimized width
- **Mobile**: Full-width single column with touch-friendly buttons

## 🔐 Security Considerations

### Google Maps API Key
1. Always restrict API key to your domain
2. Use environment variables for sensitive keys
3. Never commit API keys to git
4. Regenerate keys if compromised

### User Data
- No personal data is stored
- Location is only used for current session
- No health information is retained

## 🐛 Troubleshooting

### Map Not Showing?
- Verify Google Maps API key is correct
- Check browser console for errors
- Ensure Places API is enabled

### Symptoms Not Found?
- Type the exact symptom name
- Use common medical terms
- Check if symptom exists in training data

### No Specialists Found?
- Verify location is correct
- Try a larger city name
- Check if specialists exist in your area

### Geolocation Not Working?
- Allow browser permission to access location
- Use HTTPS in production
- Check browser location settings

## 📚 API Endpoints

### `/api/symptoms` (GET)
Returns list of available symptoms

### `/predict` (POST)
Predicts disease from symptoms
```json
{
  "symptoms": {
    "headache": 1,
    "fever": 1,
    "cough": 0
  }
}
```

### `/api/search_symptoms` (POST)
Searches and matches symptoms from text
```json
{
  "text": "headache and fever"
}
```

### `/health` (GET)
Health check endpoint

## 📦 File Structure

```
project/
├── app.py                 # Flask app with API endpoints
├── templates/
│   └── index.html        # Consumer-friendly UI with Maps
├── Models/
│   ├── best_model.pkl    # Trained disease classifier
│   ├── disease_encoder.pkl
│   ├── feature_scaler.pkl
│   └── all_symptoms.txt
├── disease_specialist_mapping.py  # Disease-specialist mapping
├── requirements.txt      # Python dependencies
├── GOOGLE_MAPS_SETUP.md  # Google Maps setup guide
└── README.md            # This file
```

## 🎓 How ML Model Works

1. **Symptom Encoding**: Converts selected symptoms to feature vector (0/1)
2. **Feature Scaling**: Normalizes features using trained scaler
3. **Prediction**: ML model predicts disease class with probability
4. **Confidence**: Shows probability score as confidence %
5. **Alternatives**: Returns top 5 predictions ranked by probability

## 🚀 Deployment

### Heroku Deployment
```bash
heroku create your-app-name
heroku config:set GOOGLE_MAPS_API_KEY=YOUR_KEY
git push heroku main
```

### AWS/DigitalOcean
1. Set environment variable with API key
2. Configure domain in Google Maps console
3. Deploy Flask app

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## 📞 Support & Contact

For issues or questions:
1. Check GOOGLE_MAPS_SETUP.md for Maps-related issues
2. Review troubleshooting section
3. Check Flask logs for errors
4. Verify all model files are present

## 📄 License

Your Project License Here

## ✅ Version History

### v2.0 (Current)
- ✨ Added Google Maps integration
- ✨ Search box with autocomplete
- ✨ Consumer-friendly UI redesign
- ✨ Mobile-responsive design
- 🔧 Improved symptom matching
- 🔧 Better error handling

### v1.0
- Initial disease prediction system
- Checkbox-based symptom selection
- Specialist recommendations

---

**Enjoy helping patients find their diagnosis!** 🏥✨
