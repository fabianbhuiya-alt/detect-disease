# Google Maps Integration Setup Guide

## Overview
Your updated Symptom Checker now includes **Google Maps integration** to help consumers find specialists and hospitals near them.

## Step 1: Get Google Maps API Key

### 1.1 Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown at the top
3. Click **NEW PROJECT**
4. Enter project name: `Symptom Checker Maps`
5. Click **CREATE**

### 1.2 Enable Required APIs
1. In the search bar at the top, search for **"Maps JavaScript API"**
2. Click **ENABLE** on the Maps JavaScript API page
3. Search for **"Places API"**
4. Click **ENABLE** on the Places API page
5. Search for **"Geocoding API"**
6. Click **ENABLE** on the Geocoding API page

### 1.3 Create API Key
1. In the left sidebar, click **Credentials**
2. Click **+ CREATE CREDENTIALS**
3. Select **API Key**
4. Copy the generated API key

## Step 2: Configure Your Application

### Option A: Using Environment Variable (Recommended for Production)
1. Create a `.env` file in your project root:
```bash
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
```

2. Update `app.py` to use it:
```python
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
```

3. Install python-dotenv:
```bash
pip install python-dotenv
```

### Option B: Direct Configuration (Development Only)
1. Open `templates/index.html`
2. Find this line (around line 3):
```html
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDemoKey123&libraries=places"></script>
```

3. Replace `AIzaSyDemoKey123` with your actual API key:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY_HERE&libraries=places"></script>
```

## Step 3: API Key Restrictions (For Security)

### Restrict Key to Your Domain
1. Go back to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Credentials** → Find your API key
3. Click on your key to edit it
4. Under **Key restrictions**, select **HTTP referrers (web sites)**
5. Add your website URL: `http://localhost:5000/*`
6. For production, add your domain: `https://yourdomain.com/*`

### Restrict to Specific APIs
1. Under **API restrictions**, select **Restrict key**
2. Select these APIs:
   - Maps JavaScript API
   - Places API
   - Geocoding API

## Step 4: Set Up Local Development

### Using .env file approach:
```bash
# Create .env
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE

# Install dependency
pip install python-dotenv

# Update app.py line 7:
from dotenv import load_dotenv
load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
```

### Test Configuration
```bash
# Run your app
python app.py

# Visit http://localhost:5000
# Try the symptom checker and test the map functionality
```

## Features Enabled by Google Maps

✅ **Find Specialists Near You**: Search for specialists by your location
✅ **Automatic Location Detection**: Use current GPS location (with permission)
✅ **Map Markers**: Shows hospital/clinic locations with ratings
✅ **Info Windows**: Click markers to see details (name, address, rating)
✅ **Address Search**: Enter any city or address to search nearby

## Troubleshooting

### Map Not Showing
- **Cause**: API key not configured
- **Solution**: Verify API key in index.html or environment variable

### "Google is not defined" Error
- **Cause**: API script failed to load
- **Solution**: Check if API key is valid and has proper restrictions

### Places Not Found
- **Cause**: Places API not enabled
- **Solution**: Go to Google Cloud Console and enable Places API

### Geolocation Not Working
- **Cause**: Browser permission denied
- **Solution**: Allow location access in browser settings

## Billing Considerations

Google Maps APIs have free tier quotas:
- **Maps JavaScript API**: Free tier includes $7 free credit/month (covers most usage)
- **Places API**: Free tier includes ~1,000 calls/day
- **Geocoding API**: Free tier includes ~25,000 calls/day

Monitor your usage in [Google Cloud Console](https://console.cloud.google.com/billing).

## File Structure After Setup

```
your_project/
├── app.py (updated with API key support)
├── templates/
│   └── index.html (updated with maps)
├── .env (create this - contains API key)
├── requirements.txt
└── GOOGLE_MAPS_SETUP.md (this file)
```

## Next Steps

1. ✅ Get Google Maps API key
2. ✅ Configure your application
3. ✅ Test the symptom checker
4. ✅ Customize specialist search radius (in index.html line ~500, change `radius: 5000` to different value in meters)
5. ✅ Deploy to production with proper domain restrictions

## Support

For more information:
- [Google Maps Documentation](https://developers.google.com/maps/documentation)
- [Places API Guide](https://developers.google.com/maps/documentation/places/web-service/overview)
- [Geocoding API Guide](https://developers.google.com/maps/documentation/geocoding/overview)
