# 🚀 Quick Start Guide

Get your AI Symptom Checker up and running in 5 minutes!

## ⚡ 5-Minute Setup

### Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

### Step 2: Get Google Maps API Key (2 min)
👉 **Follow the detailed guide:** [GOOGLE_MAPS_SETUP.md](GOOGLE_MAPS_SETUP.md)

**Quick Summary:**
1. Go to https://console.cloud.google.com/
2. Create a new project
3. Enable these APIs:
   - Maps JavaScript API
   - Places API
   - Geocoding API
4. Create an API key
5. Copy your API key

### Step 3: Configure API Key (1 min)

**Option A: Using Environment File (Recommended)**
```bash
# Create .env file and add:
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
```

**Option B: Direct in HTML**
1. Open `templates/index.html`
2. Find line 3: `<script src="https://maps.googleapis.com/maps/api/js?key=...`
3. Replace the key with your actual key

### Step 4: Run the App (1 min)
```bash
python app.py
```

### Step 5: Open in Browser
```
http://localhost:5000
```

✅ **You're done!** 🎉

---

## 📝 How to Use the App

### Describe Your Symptoms
1. Type a symptom in the search box (e.g., "headache")
2. See suggestions appear instantly
3. Click a suggestion or press Enter to add it
4. Add multiple symptoms for better accuracy

### Check Your Disease
1. Click **🔍 Check Disease** button
2. AI analyzes your symptoms
3. See the predicted disease and confidence level

### Find Specialists Near You
1. Click on a specialist badge
2. **Or** enter your city in the search box and click "Search"
3. Map shows all nearby specialists
4. Click markers for details, ratings, and address

### Use Your Location
- Click **Use My Location** to auto-detect your GPS coordinates
- System finds specialists nearby automatically

---

## 🎯 Example Scenarios

### Scenario 1: Headache and Fever
```
1. Type: "headache" → Click suggestion
2. Type: "fever" → Click suggestion
3. Click "Check Disease"
4. Result: Could be flu or migraine
5. Recommends: Neurologist or General Practitioner
6. Find nearby in your city
```

### Scenario 2: Skin Issues
```
1. Type: "rash"
2. Type: "itching"
3. Click "Check Disease"
4. Result: Could be eczema or psoriasis
5. Recommends: Dermatologist
6. Find dermatologists near you
```

### Scenario 3: Heart Issues
```
1. Type: "chest pain"
2. Type: "shortness of breath"
3. Click "Check Disease"
4. Result: Could be angina or heart condition
5. Recommends: Cardiologist
6. Find cardiologists (URGENT!)
```

---

## 🔧 Common Issues & Solutions

### Google Maps Not Showing?
**Problem:** Map is blank or shows errors
**Solution:** 
1. Check if API key is correct
2. Verify Places API is enabled
3. Open browser console (F12) for error messages

### Symptoms Not Appearing?
**Problem:** Can't find the symptom you're looking for
**Solution:**
1. Try a different term (e.g., "fever" instead of "high temperature")
2. Check if it's a common medical term
3. The symptom must be in your training dataset

### Geolocation Not Working?
**Problem:** "Use My Location" button doesn't work
**Solution:**
1. Allow browser access to location
2. Check browser location settings
3. Try entering address manually instead

### API Key Error?
**Problem:** "This API project is not authorized"
**Solution:**
1. Go to Google Cloud Console
2. Check API key is correct
3. Verify all required APIs are enabled
4. Wait a few minutes after enabling APIs (they need time to propagate)

---

## 📚 File Overview

| File | Purpose |
|------|---------|
| `app.py` | Main Flask server with prediction API |
| `templates/index.html` | Consumer-friendly UI with Google Maps |
| `disease_specialist_mapping.py` | Disease-to-specialist mapping |
| `requirements.txt` | Python dependencies |
| `.env.example` | Example environment variables |
| `Models/` | Trained ML models |
| `GOOGLE_MAPS_SETUP.md` | Detailed Maps setup guide |
| `SYSTEM_README.md` | Full documentation |

---

## 🎨 UI Features

✅ **Search Box with Autocomplete**
- Type symptoms and see suggestions in real-time
- Press Enter or click to add
- Remove symptoms with ×

✅ **Disease Prediction**
- Shows most likely disease
- Confidence level with progress bar
- Lists alternative conditions

✅ **Specialist Finder**
- Recommends doctors for your condition
- Click to search on Google Maps
- Shows hospitals with ratings

✅ **Google Maps Integration**
- Find specialists in your area
- Use GPS or enter address
- See markers for all nearby clinics
- View details, ratings, and directions

✅ **Mobile Friendly**
- Works on phones, tablets, desktops
- Touch-friendly buttons
- Responsive layout

---

## 🔐 Security Notes

1. **API Key Safety**
   - Never commit .env file to Git
   - Use environment variables
   - Restrict key to your domain

2. **User Privacy**
   - No health data is stored
   - Location only used for current session
   - No tracking or logging

---

## 🚀 Next Steps

### 1. Test Thoroughly
- Try different symptom combinations
- Test on mobile devices
- Verify maps work in your location

### 2. Customize (Optional)
- Change colors in `templates/index.html` CSS
- Adjust search radius (line ~525)
- Add more disease-specialist mappings

### 3. Deploy (When Ready)
- See SYSTEM_README.md for deployment options
- Use environment variables for API keys
- Test on production domain

### 4. Monitor
- Check Google Cloud Console for API usage
- Monitor Flask logs for errors
- Track user feedback

---

## 📞 Need Help?

1. **Google Maps Issues?** → See GOOGLE_MAPS_SETUP.md
2. **Features & Usage?** → See SYSTEM_README.md
3. **API Documentation?** → Open app.py and read comments
4. **Still Stuck?** → Check browser console (F12 → Console tab)

---

## 🎉 Success Checklist

✅ Python packages installed
✅ Google Maps API key created
✅ API key configured in app
✅ App running (http://localhost:5000)
✅ Can search symptoms
✅ Can see disease predictions
✅ Maps work and show nearby specialists
✅ Try a few different symptom combinations

**If all checks pass - you're all set!** 🏥✨

---

**Enjoy your AI Symptom Checker!**

Built with ❤️ using Flask, Machine Learning, and Google Maps
