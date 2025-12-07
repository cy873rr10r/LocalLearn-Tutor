# 🚀 Quick Start Guide - LocalLearn

## Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
cd /media/cybter/Software/ADK-Project/LocalLearn-AI
pip install -r requirements.txt
```

Or use the setup script:
```bash
./setup.sh
```

### Step 2: Run the App
```bash
streamlit run main.py
```

### Step 3: Open in Browser
Navigate to: **http://localhost:8501**

---

## First-Time Usage

1. **Select Language**: Choose from dropdown (e.g., Hindi, Tamil, Kannada)
2. **Type Topic**: Enter "Newton's First Law"
3. **Click "🎯 Explain"**
4. **Read & Listen**: View explanation and click audio to hear it
5. **Make Simpler** (Optional): Click "🔍 Make Even Simpler" for shorter version

---

## What You'll See

### Beautiful UI
- **Banner**: "LocalLearn – Science in Your Language & Style"
- **Clean Layout**: Topic input, language selector, action buttons
- **Output Box**: Styled explanation with local dialect
- **Audio Player**: Text-to-speech in selected language

### Features to Try

✅ **Text Input**: Type any science topic  
✅ **Language Selection**: 11 languages with regional context  
✅ **Explain Button**: Get dialect-aware explanation  
✅ **Simplify Button**: Get even simpler version (5-6 sentences)  
✅ **Image Upload**: Upload textbook photo (then type topic)  
✅ **Audio Output**: Listen to explanation in local accent  
✅ **Clear Button**: Reset and try another topic  

---

## Example Flow

1. **Select**: Hindi
2. **Type**: "Gravity"
3. **Click**: 🎯 Explain
4. **Get Output**: 
   ```
   अरे यार, जब तू मोबाइल हाथ से गिरा देता है, तो नीचे क्यों गिरता है? 
   ऊपर क्यों नहीं उड़ता? यही है gravity!
   
   पृथ्वी सभी चीजों को अपनी तरफ खींचती है। Cricket में जब bowler 
   ball ऊपर फेंकता है, वो वापस नीचे आ जाती है। Bus में सामान ऊपर 
   rack पर रखते हो, तो वो नीचे नहीं उड़ता। यही gravity का effect है।
   ```
5. **Listen**: Click audio player
6. **Simplify**: Click "🔍 Make Even Simpler" for shorter version

---

## Test Topics (Copy-Paste These)

### Physics
- Newton's First Law
- Gravity
- Light and Reflection
- Sound Waves
- Kinetic Energy

### Chemistry
- Photosynthesis
- Acids and Bases
- Chemical Reactions
- Water Cycle

### Biology
- Cell Division
- Human Digestive System
- DNA Structure
- Respiration

### Math
- Pythagoras Theorem
- Area and Perimeter
- Fractions
- Algebraic Equations

---

## Troubleshooting

### App won't start?
```bash
# Check if streamlit is installed
pip list | grep streamlit

# Reinstall if needed
pip install streamlit --force-reinstall
```

### ADK errors?
```bash
# Check ADK installation
pip list | grep adk

# Install if missing
pip install google-adk
```

### Audio not working?
- Check internet connection (gTTS needs online access)
- Try different browser
- Check browser audio permissions

---

## Advanced Usage

### Upload Textbook Photo
1. Click "Browse files" under "📸 Or upload a textbook photo"
2. Select image (PNG, JPG, JPEG)
3. View uploaded image
4. **Type the topic** from the image
5. Click "🎯 Explain"

*Note: OCR is optional feature - manual typing works best*

### Try Different Languages
Same topic in different languages shows how regional examples change:

**Hindi**: Cricket, chai shops, bus travel  
**Tamil**: Filter coffee, auto rides, temple visits  
**Kannada**: BMTC buses, tech parks, coffee estates  

---

## Pro Tips

💡 **Be Specific**: "Newton's First Law" > "Physics"  
💡 **Use Simplify Wisely**: Get detailed first, then simplify  
💡 **Try All Languages**: See regional examples for same topic  
💡 **Listen to Audio**: Helps with pronunciation  
💡 **Upload Photos**: Visual reference helps  

---

## What Makes It Special?

**Not Translation** ❌  
```
Newton का पहला नियम कहता है कि...
```

**Local Teaching** ✅  
```
अरे भाई, बस में खड़े हो और brake मारता है तो...
```

---

## Need Help?

- Read: `README.md` for full documentation
- See: `EXAMPLES.md` for example outputs
- Check: Project structure in `README.md`

---

**Ready to start? Run the app!**

```bash
streamlit run main.py
```

**Then visit: http://localhost:8501**

🌍 **Making science accessible in every language!**
