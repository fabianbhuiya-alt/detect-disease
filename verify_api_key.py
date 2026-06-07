#!/usr/bin/env python
"""
Google Maps API Key Verification Script
Run this to verify your Google Maps API key is configured correctly
"""

import os
from dotenv import load_dotenv

print("=" * 60)
print("🔍 Google Maps API Key Verification")
print("=" * 60)

# Load environment variables
load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY', 'NOT_SET')

print("\n1️⃣  Checking .env file...")
if os.path.exists('.env'):
    print("   ✅ .env file exists")
else:
    print("   ❌ .env file NOT found!")
    print("   💡 Copy .env.example to .env and add your API key")

print("\n2️⃣  Checking API Key...")
if api_key == 'NOT_SET':
    print("   ❌ GOOGLE_MAPS_API_KEY not set!")
    print("   💡 Add this to your .env file:")
    print("      GOOGLE_MAPS_API_KEY=YOUR_KEY_HERE")
elif api_key == 'YOUR_API_KEY_HERE':
    print("   ⚠️  GOOGLE_MAPS_API_KEY is placeholder!")
    print("   💡 Replace with your actual API key from Google Cloud Console")
    print("      Get key from: https://console.cloud.google.com/")
else:
    print(f"   ✅ API Key found: {api_key[:20]}...")
    print(f"   Full key length: {len(api_key)} characters")

print("\n3️⃣  Checking API Key Format...")
if api_key.startswith('AIza'):
    print("   ✅ API Key format looks correct (starts with 'AIza')")
elif api_key != 'NOT_SET' and api_key != 'YOUR_API_KEY_HERE':
    print("   ⚠️  API Key format may be incorrect")
    print("   💡 Key should start with 'AIza'")

print("\n4️⃣  What to do next...")
print("   a) Make sure you have a .env file with your API key:")
print("      GOOGLE_MAPS_API_KEY=your_actual_key")
print("")
print("   b) Restart Flask app:")
print("      python app.py")
print("")
print("   c) Check the output for:")
print("      ✓ Google Maps API Key configured: AIza...")
print("")
print("   d) If still not working:")
print("      - Check browser console (F12 → Console)")
print("      - Verify API key is valid on Google Cloud Console")
print("      - Ensure Places API is enabled")
print("      - Check if key is restricted to specific domains")

print("\n5️⃣  Verify in Browser...")
print("   a) Open http://localhost:5000")
print("   b) Press F12 to open Developer Tools")
print("   c) Go to Console tab")
print("   d) Look for any red errors about Google Maps")
print("   e) Test the app:")
print("      - Type a symptom")
print("      - Click 'Check Disease'")
print("      - Try to find specialists on map")

print("\n" + "=" * 60)
print("Need more help? See GOOGLE_MAPS_SETUP.md")
print("=" * 60 + "\n")
