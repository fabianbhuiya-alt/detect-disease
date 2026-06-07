# 🔧 Fix: "This page didn't load Google Maps correctly"

## 🚨 Problem
You're seeing this error message:
```
"This page didn't load Google Maps correctly. 
See the JavaScript console for technical details"
```

This happens because your **Google Maps API key is not properly configured**.

---

## ✅ Solution (5 Steps)

### Step 1: Create .env File
In your project root folder, create a file named `.env` (if it doesn't exist):

**Windows:**
```cmd
# In PowerShell or Command Prompt
type nul > .env
```

**Mac/Linux:**
```bash
touch .env
```

---

### Step 2: Add Your API Key to .env
Open the `.env` file and add:
```
GOOGLE_MAPS_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

**Example:**
```
GOOGLE_MAPS_API_KEY=AIzaSyDK9e0a1b2c3d4e5f6g7h8i9j0k
```

---

### Step 3: Get Google Maps API Key (If You Don't Have One)

#### 3a) Go to Google Cloud Console
https://console.cloud.google.com/

#### 3b) Create a New Project
- Click project dropdown
- Click "NEW PROJECT"
- Name: "Symptom Checker Maps"
- Click CREATE

#### 3c) Enable Required APIs
1. Search bar at top → Search "Maps JavaScript API"
2. Click ENABLE
3. Search "Places API" → ENABLE
4. Search "Geocoding API" → ENABLE

#### 3d) Create API Key
1. Left sidebar → Click "Credentials"
2. Click "+ CREATE CREDENTIALS"
3. Click "API Key"
4. Copy the key (looks like: AIzaSy...)

---

### Step 4: Verify Configuration
Run the verification script:

**Windows:**
```cmd
python verify_api_key.py
```

**Mac/Linux:**
```bash
python3 verify_api_key.py
```

You should see:
```
✅ API Key found: AIza...
✅ API Key format looks correct
```

---

### Step 5: Restart Your App

**Stop the current app:**
```
Press Ctrl+C in terminal
```

**Start the app again:**
```cmd
python app.py
```

You should see:
```
✓ Google Maps API Key configured: AIza...
```

---

## 🧪 Test It Works

1. Open http://localhost:5000
2. Type a symptom (e.g., "fever")
3. Click "Check Disease"
4. Scroll down to "Find Specialists Near You"
5. Enter a city (e.g., "New York")
6. Click "Search"
7. **Map should show with markers** ✅

---

## 🐛 Still Not Working?

### Check 1: Browser Console
1. Open http://localhost:5000
2. Press **F12** (or Cmd+Option+I on Mac)
3. Click **Console** tab
4. Look for red error messages
5. Screenshot any errors

### Check 2: .env File
```bash
# Make sure .env exists and has your key
cat .env
# Should show: GOOGLE_MAPS_API_KEY=AIzaSy...
```

### Check 3: Flask Startup Output
When you run `python app.py`, you should see:
```
✓ Google Maps API Key configured: AIza...
```

If you see:
```
⚠️  WARNING: Google Maps API Key is not configured!
```

Then your .env file is not being read. Make sure:
- File is named `.env` (not `.env.txt` or `.env.example`)
- File is in project root directory
- File contains: `GOOGLE_MAPS_API_KEY=YOUR_KEY`

### Check 4: API Key Restrictions
1. Go to Google Cloud Console
2. Click your API key
3. Check "API restrictions"
4. Make sure "Maps JavaScript API", "Places API", "Geocoding API" are selected
5. Or select "Restrict key"

### Check 5: Domain Restrictions
1. Go to Google Cloud Console
2. Click your API key
3. Check "Key restrictions"
4. Make sure it says "HTTP referrers (web sites)"
5. Add: `http://localhost:5000/*`

---

## 📋 Quick Checklist

- [ ] .env file exists in project root
- [ ] .env contains: `GOOGLE_MAPS_API_KEY=AIzaSy...`
- [ ] API key starts with "AIza"
- [ ] Maps JavaScript API is enabled
- [ ] Places API is enabled
- [ ] Geocoding API is enabled
- [ ] Flask app restarted after .env created
- [ ] Console shows: "✓ Google Maps API Key configured"

---

## ✨ If All Checks Pass

Your app should now work! Try:
1. Type "fever" 
2. Click "Check Disease"
3. See disease prediction
4. Enter city like "New York"
5. Click "Search"
6. **See map with hospitals** ✅

---

## 📞 Still Need Help?

1. Check: **GOOGLE_MAPS_SETUP.md** (detailed setup guide)
2. Check: **verify_api_key.py** (automated verification)
3. Check browser console for specific error messages
4. Make sure APIs are enabled in Google Cloud Console

---

**Most Common Fix:** Just run `python verify_api_key.py` to see what's missing! 🔍
