# System Architecture & Data Flow

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CONSUMER (Browser)                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Web UI (index.html)                                 │  │
│  │  • Symptom search with autocomplete                  │  │
│  │  • Disease prediction display                        │  │
│  │  • Google Map integration                            │  │
│  │  • Specialist finder                                 │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                          ↕️
                     (HTTP API)
                          ↕️
┌─────────────────────────────────────────────────────────────┐
│              BACKEND (Flask Server)                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Flask App (app.py)                                  │  │
│  │  Routes:                                             │  │
│  │  • /                    → Serve frontend             │  │
│  │  • /api/symptoms        → Get all symptoms           │  │
│  │  • /api/search_symptoms → Search/autocomplete        │  │
│  │  • /predict            → Disease prediction          │  │
│  │  • /api/specialists_map → Map data                  │  │
│  │  • /health             → Status check                │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  ML Pipeline                                         │  │
│  │  • Feature Scaler → Scale symptoms                   │  │
│  │  • ML Model → Predict disease                        │  │
│  │  • Label Encoder → Convert to disease name           │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Specialist Mapping (disease_specialist_mapping.py)  │  │
│  │  Maps diseases to specialists                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
         ↕️                              ↕️
   ┌─────────────┐          ┌────────────────────────┐
   │ ML Models   │          │ Google Maps API        │
   │ (pkl files) │          │ • Places API           │
   │ • Scaler    │          │ • Geocoding API        │
   │ • Classifier│          │ • Maps JS API          │
   │ • Encoder   │          └────────────────────────┘
   └─────────────┘
```

---

## 📊 Data Flow Diagram

### 1. User Types Symptom
```
User Input: "fever"
    ↓
Frontend JavaScript captures input
    ↓
Matches against loaded symptoms array
    ↓
Displays autocomplete suggestions
    ↓
User clicks suggestion
    ↓
Symptom added to selectedSymptoms Set
    ↓
UI updates to show selected symptoms
```

### 2. Disease Prediction Flow
```
User clicks "Check Disease"
    ↓
Build feature vector (all symptoms as 0/1)
    ↓
POST /predict endpoint
    ↓
Backend scales features
    ↓
ML model predicts disease class
    ↓
Get probability scores for top 5 predictions
    ↓
Return disease + specialists + confidence
    ↓
Frontend displays results with animation
```

### 3. Specialist Map Search Flow
```
User enters location or clicks "Use My Location"
    ↓
Geocode address to coordinates (Google Geocoding API)
    ↓
Get specialist recommendations for disease
    ↓
For each specialist, search Google Places:
    • Geocoder.geocode() → location coordinates
    • PlacesService.nearbySearch() → find hospitals
    ↓
Display markers on map
    ↓
User clicks marker
    ↓
Info window shows hospital details
```

---

## 🔄 Request/Response Cycle

### Example: Predict Disease

**Client Request:**
```javascript
POST /predict
Content-Type: application/json

{
  "symptoms": {
    "fever": 1,
    "cough": 1,
    "headache": 0,
    "nausea": 0,
    ... (all symptoms)
  }
}
```

**Server Processing:**
```python
1. Extract symptoms → feature_vector
2. X = np.array([feature_vector])
3. X_scaled = scaler.transform(X)
4. pred_class = model.predict(X_scaled)[0]
5. probs = model.predict_proba(X_scaled)[0]
6. disease = le.inverse_transform([pred_class])[0]
7. specialists = get_specialist_for_disease(disease)
8. Sort probabilities for top 5
```

**Server Response:**
```json
{
  "success": true,
  "predicted_disease": "Common Cold",
  "confidence": 0.847,
  "confidence_percentage": "84.7%",
  "recommended_specialists": [
    "Internal Medicine",
    "General Practitioner"
  ],
  "top_predictions": [
    {"disease": "Common Cold", "probability": 0.847},
    {"disease": "Flu", "probability": 0.098},
    {"disease": "Allergic Rhinitis", "probability": 0.032}
  ],
  "symptoms_reported": 2,
  "total_symptoms_available": 132
}
```

**Client Display:**
```javascript
1. Update disease name
2. Set confidence bar width
3. Populate specialist badges
4. Display top predictions list
5. Show results section with animation
```

---

## 🗺️ Google Maps Integration Flow

```
User has disease prediction
    ↓
User enters location: "New York, NY"
    ↓
Frontend calls searchSpecialists(location)
    ↓
JavaScript Geocoder.geocode(address)
    ↓
Google returns: { lat: 40.7128, lng: -74.0060 }
    ↓
Map center moves to location
    ↓
For each recommended specialist:
    ↓
PlacesService.nearbySearch({
  location: { lat, lng },
  radius: 5000,
  keyword: "Cardiologist"
})
    ↓
Google Places API returns 20 results
    ↓
Frontend creates markers for each result
    ↓
Add info window with:
    • Hospital name
    • Address
    • Rating
    • Review count
    ↓
Display markers on map
    ↓
User clicks marker → Info window opens
```

---

## 📂 State Management

### Frontend State (JavaScript)
```javascript
Global Variables:
├── selectedSymptoms (Set)      → Currently selected symptoms
├── allSymptoms (Array)         → All available symptoms
├── map (Google Map)            → Map instance
├── currentMarkers (Array)      → Active map markers
├── currentSpecialists (Array)  → Current disease specialists
└── currentDiseases (Array)     → Currently predicted diseases

DOM Elements:
├── #symptomSearch             → Search input
├── #autocompleteList          → Autocomplete dropdown
├── #selectedSymptomsContainer → Selected symptoms display
├── #loading                   → Loading spinner
├── #results                   → Results display
├── #map                       → Map container
└── #fullResults              → Full results section
```

### Backend State (Flask)
```python
Loaded Resources:
├── model            → Trained classifier
├── le              → Label encoder
├── scaler          → Feature scaler
├── all_symptoms    → List of all symptoms

Configuration:
├── GOOGLE_MAPS_API_KEY  → API key (from .env)
├── CORS enabled         → Allow cross-origin requests
└── Debug mode           → For development
```

---

## 🔐 Security Flow

```
User Input: "fever"
    ↓
Frontend: Validate (only allow text)
    ↓
Frontend: Sanitize (prevent XSS)
    ↓
Match against known symptoms only
    ↓
Only send valid symptoms to backend
    ↓
Backend: Validate symptom names
    ↓
Only process known symptoms
    ↓
API responses are JSON (no HTML injection)
    ↓
Google Maps API key restricted:
    • To specific domains
    • To specific APIs
    • HTTP referrers only
```

---

## 📡 API Endpoint Specifications

### GET /api/symptoms
**Purpose:** Load all available symptoms on page load
```
Response: {
  "symptoms": ["fever", "headache", "cough", ...],
  "total": 132
}
```

### POST /api/search_symptoms
**Purpose:** Search symptoms as user types
```
Request: { "text": "fev" }
Response: {
  "query": "fev",
  "symptoms": ["fever", "high fever", "fever with chills"],
  "exact_matches": ["fever"],
  "total_available": 132
}
```

### POST /predict
**Purpose:** Predict disease from symptoms
```
Request: {
  "symptoms": {
    "fever": 1,
    "cough": 1,
    ...all other symptoms
  }
}
Response: {
  "success": true,
  "predicted_disease": "Common Cold",
  "confidence": 0.847,
  "confidence_percentage": "84.7%",
  "recommended_specialists": ["Internal Medicine"],
  "top_predictions": [...],
  "symptoms_reported": 2,
  "total_symptoms_available": 132
}
```

### GET /api/specialists_map
**Purpose:** Get specialist info for map
```
Response: {
  "google_maps_api_key": "AIzaSy...",
  "specialists": ["Cardiologist", "Internal Medicine"],
  "disease": "heart disease",
  "search_types": ["Cardiologist near me", "Internal Medicine near me"]
}
```

### GET /health
**Purpose:** Health check
```
Response: {
  "status": "healthy",
  "model_loaded": true,
  "symptoms_available": 132,
  "diseases_available": 45
}
```

---

## ⚡ Performance Metrics

### Load Time
- Page Load: ~1-2 seconds
- Symptoms Load: ~500ms
- API Response Time: ~100-200ms
- Map Render: ~1 second
- Marker Display: ~500-1000ms

### Memory Usage
- Frontend State: ~5-10 MB
- All Symptoms Array: ~2 MB
- Map Instance: ~3 MB
- Total Page: ~15-20 MB

### Database/Storage
- Model Files: ~50-100 MB total
- Symptoms List: ~2 MB
- No user database (stateless)

---

## 🔄 Caching Strategy

### Frontend Caching
```javascript
// Load once on page init
allSymptoms = [fetch from API]

// Use in-memory for autocomplete
No server calls for each keystroke

// Map instance
Reuse same map object
Just update center and markers
```

### Backend Caching (Optional)
```python
# All model files loaded once at startup
# No dynamic reloading
# Good for production performance

# Could add Redis for:
# - Symptom search results
# - Prediction results
# - Place results (optional)
```

---

## 🚀 Scalability Considerations

### For 100 concurrent users:
- Load balancing: Multiple Flask instances
- API gateway: Nginx or AWS ALB
- Caching: Redis for frequent searches
- Database: Optional for user tracking

### For 1000 concurrent users:
- Microservices: Separate prediction service
- Message queue: RabbitMQ for async predictions
- CDN: For static assets (HTML, CSS, JS)
- Analytics: Track API usage and errors

### For 10000+ concurrent users:
- Kubernetes: Container orchestration
- DynamoDB: For scalable storage
- Lambda: For serverless prediction
- CloudFront: Global CDN distribution

---

**This architecture is designed for simplicity, speed, and easy deployment! 🚀**
