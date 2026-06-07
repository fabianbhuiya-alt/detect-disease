# 👥 User Journey & Visual Guide

## 🎬 Complete User Flow

### Step 1: User Arrives at App
```
URL: http://localhost:5000
      ↓
Page loads with:
┌─────────────────────────────────────────┐
│     🏥 Symptom Checker                  │
│  Describe your symptoms and find help   │
└─────────────────────────────────────────┘

Left Panel:                   Right Panel:
┌──────────────────┐         ┌──────────────────┐
│ 💬 Describe Your │         │ 📊 Results       │
│    Symptoms      │         │                  │
│                  │         │ (No data yet)    │
│ [Search box] ▼   │         │                  │
│ No symptoms yet  │         │                  │
│                  │         │                  │
│ [Check][Clear]   │         │ 💡 Tip: Type... │
└──────────────────┘         └──────────────────┘
```

### Step 2: User Types First Symptom
```
User: Types "fever"
      ↓
System: Shows matching symptoms
      ↓
┌─────────────────────────────────────────┐
│ [fever                    ] ▼            │ ← Search box
│ ┌─────────────────────────────────────┐ │
│ │ fever                               │ │ ← Autocomplete
│ │ high fever                          │ │   suggestions
│ │ fever with chills                   │ │
│ │ fever and rash                      │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘

User: Clicks "fever" or presses Enter
      ↓
System: Adds to selected symptoms
      ↓
[fever ×]  ← Shows as tag
```

### Step 3: Add More Symptoms
```
User: Types "cough"
      ↓
[cough                    ] ▼

Select "dry cough" from suggestions
      ↓
[fever ×] [dry cough ×]

User: Types "headache"
      ↓
[headache                 ] ▼

Select "headache" from suggestions
      ↓
[fever ×] [dry cough ×] [headache ×]

← Selected symptoms area shows all additions
← Each has × button to remove
```

### Step 4: Check Disease
```
User: Clicks "🔍 Check Disease" button
      ↓
Right panel shows loading spinner
      ↓
┌──────────────────────────┐
│      Loading...          │
│        ⊙ spinning        │
│  Analyzing symptoms...   │
└──────────────────────────┘

Server: Processes symptoms
  1. Creates feature vector
  2. Scales features
  3. Runs ML model
  4. Gets predictions
  5. Matches specialists
      ↓ (< 500ms)
      ↓
Results appear with animation
```

### Step 5: View Prediction Results
```
Right Panel updates to:

┌──────────────────────────────────────────┐
│  📊 Results                              │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │ Flu                                │ │ ← Disease name
│  │ Based on your symptoms             │ │
│  │                                    │ │
│  │ Confidence Level                   │ │
│  │ ████████████░░░ 85%               │ │ ← Progress bar
│  └────────────────────────────────────┘ │
│                                          │
│  💡 Tip: Type each symptom...          │
└──────────────────────────────────────────┘
```

### Step 6: Scroll Down for Full Results
```
┌──────────────────────────────────────────┐
│  👨‍⚕️ Recommended Specialists            │
│                                          │
│  [Internal Medicine] [General Prac]      │ ← Click any
│                                          │
│  Click on a specialist to find them      │
│  nearby                                  │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│  📍 Find Specialists Near You           │
│                                          │
│  [Enter city/address___] [Search] [GPS]  │ ← Map controls
│                                          │
│  ┌────────────────────────────────────┐ │
│  │                                    │ │
│  │         Google Map                 │ │
│  │    (Shows hospital markers)        │ │
│  │          📍 📍 📍                  │ │
│  │                                    │ │
│  │                                    │ │
│  └────────────────────────────────────┘ │
│                                          │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│  🔝 Other Possible Conditions           │
│                                          │
│  • Common Cold: 85%                      │
│  • Pneumonia: 10%                        │
│  • Bronchitis: 5%                        │
│                                          │
└──────────────────────────────────────────┘
```

### Step 7: Search for Specialists on Map
```
Scenario A: Click on a specialist badge
├─ System uses current location or
├─ Shows error: "Please enter a location"
└─ User should enter address first

Scenario B: Enter location and search
├─ User enters: "San Francisco, CA"
├─ Clicks "Search" button
├─ System geocodes address
├─ Finds 5 specialists per type within 5km
├─ Displays markers on map
└─ Each marker shows hospital details

Scenario C: Use "Use My Location"
├─ Browser asks for permission
├─ User allows (or denies)
├─ If allowed:
│  ├─ Gets GPS coordinates
│  ├─ Centers map on user
│  ├─ Auto-searches for specialists
│  └─ Shows nearby hospitals
├─ If denied:
│  └─ User must enter address manually
```

### Step 8: View Hospital Details
```
User: Clicks on a map marker
      ↓
Info window appears:

┌──────────────────────────────────────┐
│ St. Mary's Hospital                  │
│ 123 Main St, San Francisco, CA 94110 │
│ ⭐⭐⭐⭐⭐ 4.8/5 (342 reviews)        │ ← Rating
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ You can:                             │
│ • Click to see more details          │
│ • Get directions (opens Maps app)    │
│ • See reviews (opens Google Places)  │
│ • Call hospital                      │
└──────────────────────────────────────┘
```

### Step 9: Try Another Symptom Search
```
User: Clicks "Clear All" button
      ↓
┌─ All symptoms removed
├─ Search box cleared
├─ Results hidden
├─ Ready for new search
└─ Predict button disabled (no symptoms)

User: Starts over with different symptoms
      ↓
New disease prediction flow
```

---

## 📱 Mobile View

### Mobile Layout (Single Column)
```
Screen Width: < 768px

┌──────────────────────────┐
│  🏥 Symptom Checker      │ ← Header
│  Describe your symptoms  │
└──────────────────────────┘

┌──────────────────────────┐
│  💬 Describe Symptoms    │ ← Full width
│                          │
│  [fever             ] ▼  │ ← Search box
│  ⊘ Autocomplete list    │
│                          │
│  [fever ×]              │ ← Tags
│                          │
│  [Check] [Clear]        │ ← Buttons
│                          │
│  [📊 Results Preview]    │
│                          │
│  💡 Tips                 │
└──────────────────────────┘

┌──────────────────────────┐
│  👨‍⚕️ Specialists         │ ← After prediction
│  [Specialist] [Specialist]│
└──────────────────────────┘

┌──────────────────────────┐
│  📍 Find Near You        │
│                          │
│  [Address input...]      │
│  [Search] [GPS]          │
│                          │
│  [  Map View  ]          │
│                          │
└──────────────────────────┘

┌──────────────────────────┐
│  🔝 Other Conditions     │
│  • Disease: %            │
│  • Disease: %            │
└──────────────────────────┘
```

---

## 🎨 Visual States

### Loading State
```
┌──────────────────────────┐
│    🔄 Analyzing...       │
│                          │
│      ⊙ ⊙ ⊙ spinning     │
│                          │
│  Processing your         │
│  symptoms...             │
└──────────────────────────┘
```

### Error State
```
┌──────────────────────────┐
│ ❌ No symptoms selected  │ ← Red background
│    Select at least 1     │
└──────────────────────────┘

OR

┌──────────────────────────┐
│ ❌ Could not find        │ ← Red background
│    location. Try again.  │
└──────────────────────────┘
```

### Success State
```
✅ Symptom added
✅ Disease predicted
✅ Specialists found
✅ Map loaded
✅ Locations found
```

### Empty State
```
"No symptoms selected yet"
↓
"No specialists found"
↓
"No conditions available"

(Gray, italicized text)
```

---

## 🎯 Key User Interactions

### Mouse/Touch Events

1. **Search Box Focus**
   - Click → Box highlights with blue border
   - Shows placeholder suggestion

2. **Typing in Search**
   - Autocomplete dropdown appears immediately
   - Updates as you type
   - Disappears on focus loss

3. **Click Suggestion**
   - Symptom is added
   - Search box clears
   - Autocomplete closes
   - Symptom tag appears

4. **Click × on Tag**
   - Symptom removed instantly
   - Tag disappears
   - Button state updates if needed

5. **Click Check Disease**
   - Loading spinner appears
   - Results preview updates
   - Full results section expands (animation)

6. **Click Map Marker**
   - Info window appears
   - Shows hospital details
   - Can click for more info

7. **Enter Address**
   - Type address
   - Click Search
   - Map centers on location
   - Markers appear

8. **Click Use My Location**
   - Browser asks permission
   - If granted: Finds specialists near user
   - If denied: Shows error

---

## 📊 Before/After Comparison

### Old System (Checkbox)
```
User sees: 100+ checkboxes in a list
User scrolls: Trying to find "fever"
User clicks: Many checkboxes
Time taken: 3-5 minutes
Frustration: High
Mobile experience: Poor
```

### New System (Search Box)
```
User sees: Clean search box + results
User types: "fever" → Instantly sees suggestions
User clicks: 1 suggestion
Time taken: 30 seconds
Frustration: None
Mobile experience: Excellent
```

---

## 💡 Smart Features Highlighted

### Feature 1: Autocomplete
```
User types: "h"
Shows: Nothing yet (< 2 chars)

User types: "he"
Shows: "headache", "heartburn", "hearing loss"

User types: "hea"
Shows: "headache", "heartburn", "hearing loss"

User types: "head"
Shows: "headache"

User types: "fever"
Shows: "fever", "high fever", "fever with chills"
```

### Feature 2: Real-time Feedback
```
Selected: 0 symptoms
Button: DISABLED (gray, not clickable)

Selected: 1+ symptoms
Button: ENABLED (colored, clickable)

Predicting: (loading spinner shows)
Results: Flash in with animation
```

### Feature 3: Map Integration
```
Before search: Default world map
After search: Centers on user location
With specialists: Shows markers
Click marker: Shows details
Zoom controls: User can explore
```

---

## 🔄 User Paths

### Path 1: Quick Health Check
1. Opens app
2. Types "fever"
3. Clicks "Check"
4. Sees disease prediction
5. Done (2 minutes)

### Path 2: Detailed Search + Specialist Finding
1. Opens app
2. Adds 3-4 symptoms
3. Checks disease
4. Finds specialists on map
5. Clicks hospital for details
6. Done (5 minutes)

### Path 3: Mobile Emergency Lookup
1. Opens app on phone
2. Types 2 symptoms quickly
3. Checks disease
4. Clicks "Use My Location"
5. Sees nearest specialist
6. Done (1 minute)

---

**Every interaction is designed to be intuitive and fast!** ⚡✨

The system guides users naturally from symptom entry → disease prediction → specialist discovery.
