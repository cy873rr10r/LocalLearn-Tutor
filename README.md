# 🌍 LocalLearn – Science in Your Language & Style

An AI-powered education app that explains any topic in your local language using **regional dialect, tone, and real-life examples** from your daily context. Powered by **Google Gemini AI**.

## ✨ Core Features

- **🌙 Dark Theme UI**: Modern black background with white text for better readability
- **11 Indian Languages**: Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Urdu, English
- **Dialect-Aware Explanations**: Uses regional slang and local context naturally (NOT just translation)
- **Real-Life Examples**: Contextual examples from cricket, farming, local transport, festivals, daily life
- **Simplification Button**: "Make Even Simpler" for ultra-simple 5-6 sentence explanations
- **🔊 Automatic Audio**: Audio is generated automatically when explanation appears (uses Google TTS with rate limits)
- **Image Upload**: Upload textbook photos (OCR optional - just type the topic)
- **Text-to-Speech**: Audio playback in selected language/accent
- **AI-Powered**: Uses Google ADK agent architecture with Gemini for intelligent, context-aware explanations

## 🎯 What Makes This Different?

**LocalLearn doesn't just translate** - it adapts the teaching style:

❌ **Bad (Translation)**: "Newton का पहला नियम कहता है कि एक वस्तु गति में बनी रहेगी..."

✅ **Good (LocalLearn)**: "अरे भाई, जब तू बस में खड़ा है ना और driver अचानक brake मारता है, तो तू आगे की तरफ झुक जाता है ना? बस यही है Newton का पहला नियम!..."

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google AI API Key (for Gemini models)

### Setup API Key

1. **Get Google AI API Key:**
   - Visit: https://makersuite.google.com/app/apikey
   - Create a new API key
   - Copy the key (should start with 'AIza')

2. **Create environment file:**
   ```bash
   cp env.example .env
   ```

3. **Edit .env file:**
   ```bash
   # Replace with your actual API key
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

4. **Test your API key:**
   ```bash
   python test_api_key.py
   ```
   This will validate your API key before running the app.

### Installation

1. **Navigate to project:**
   ```bash
   cd /media/cybter/Software/ADK-Project/LocalLearn-AI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run main.py
   ```

4. **Open browser** at `http://localhost:8501`

## 📖 How to Use

### Basic Usage

1. **Select your language** from dropdown (e.g., Hindi, Tamil, Telugu)
2. **Type any topic** (e.g., "Newton's First Law", "Photosynthesis", "Gravity")
3. Click **"🎯 Explain"**
4. Get explanation in local dialect with real-life examples
5. Click **"🔊 Listen"** to hear the explanation

### Advanced Features

#### Make Even Simpler
- After getting explanation, click **"🔍 Make Even Simpler"**
- Gets ultra-simple 5-6 sentence version with ONE main idea

#### Upload Textbook Photo (Optional)
1. Click **"Browse files"** under "Upload a textbook photo"
2. Upload photo (PNG, JPG, JPEG)
3. View the image
4. **Type the topic name** from the image
5. Click **"🎯 Explain"**

*Note: OCR is optional - just type the topic manually after viewing the image*

## 🗣️ Supported Languages & Regional Context

| Language | Regional Examples Used |
|----------|------------------------|
| **Hindi** | Cricket, bus travel, chai shops, farming, Diwali |
| **Tamil** | Temple visits, filter coffee, auto rides, Pongal |
| **Telugu** | Movies, biryani, local markets, Sankranti |
| **Bengali** | Fish markets, tram rides, Durga Puja, sweets |
| **Marathi** | Local trains, vada pav, Ganesh Chaturthi |
| **Gujarati** | Dhokla, garba, business, kite flying |
| **Kannada** | Coffee estates, BMTC buses, tech parks, Dasara |
| **Malayalam** | Coconut trees, boat rides, Onam, fish curry |
| **Punjabi** | Wheat farming, bhangra, tractors, Lohri |
| **Urdu** | Biryani, cricket, qawwali, markets |
| **English** | Daily life in India, cricket, local transport |

## 🤖 Multi-Agent Architecture

The app uses **Google ADK's Agent-to-Agent (A2A) communication**:

```
┌─────────────┐      ┌──────────────┐      ┌──────────────┐
│ Root Agent  │ ───> │ Explain Agent│ ───> │ Refiner Agent│
│ (Analyzes)  │      │ (Generates)  │      │ (Polishes)   │
└─────────────┘      └──────────────┘      └──────────────┘
```

### Agent 1: Root Agent
- Analyzes the topic
- Identifies key concepts to explain
- Selects appropriate regional examples
- Passes context to Explain Agent

### Agent 2: Explain Agent
- Generates explanation in target language
- Uses dialect-aware prompts
- Includes 2-3 real-life examples from regional context
- Avoids technical jargon
- Passes to Refiner Agent (A2A Communication)

### Agent 3: Refiner Agent
- Reviews and improves clarity
- Maintains regional dialect
- Polishes language while keeping it simple
- Ensures conversational tone
- Outputs final explanation

## 🎨 Key Implementation Details

### Dialect-Aware Prompts

Each agent receives carefully crafted prompts:

```python
prompt = f"""
Explain the topic: {topic}
Language: {language}
Tone: Friendly teaching style for beginners.
Dialect: Use regional slang/phrases naturally but keep accuracy.
Add 2-3 real-life situations from: {regional_context}
Avoid heavy technical words. Focus on simple understanding.
Do NOT just translate - adapt the teaching style for local understanding.
"""
```

### Regional Context Mapping

```python
REGIONAL_CONTEXTS = {
    "Hindi": "cricket, bus travel, chai shops, farming, festivals like Diwali",
    "Tamil": "temple visits, filter coffee, bus/auto rides, Pongal festival",
    # ... more languages
}
```

### Simplification Logic

**Normal Mode**: Detailed with 2-3 examples, conversational tone

**Simplified Mode**: 
- Maximum 5-6 sentences
- ONE main idea
- ONE clear example
- ZERO technical terms

## 🛠️ Technical Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Engine**: Google ADK (Multi-Agent Development Kit)
- **TTS**: gTTS (Google Text-to-Speech)
- **Image Processing**: Pillow (PIL)
- **Multi-Agent Communication**: ADK NodeGroup with A2A

## 🎯 Example Topics to Try

**Physics**: 
- Newton's First Law
- Gravity
- Kinetic Energy
- Friction

**Chemistry**: 
- Photosynthesis
- Chemical Bonds
- Acids and Bases

**Biology**: 
- Cell Division
- Digestive System
- DNA Structure

**Math**: 
- Pythagoras Theorem
- Fractions
- Quadratic Equations

**General Science**: 
- Water Cycle
- Solar System
- Electricity

## 🐛 Troubleshooting

### API Key Issues
```bash
# Test your API key first
python test_api_key.py
```
- **API key format**: Must start with 'AIza'
- **Get new key**: https://makersuite.google.com/app/apikey
- **Check .env file**: Ensure it's in project root
- **Copy correctly**: No extra spaces or characters

### Audio not playing
- **Rate Limiting**: Google TTS has usage limits. If you see "429 Too Many Requests", wait 5-10 minutes
- **Offline Fallback**: App automatically tries offline TTS (pyttsx3) when Google TTS fails
- **Internet Required**: Online TTS requires internet; offline TTS works without connection
- **Language Support**: Online TTS supports 11 languages; offline TTS is English-only
- **Text Length**: Very long explanations may cause issues with online TTS

### App won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+ required)
- Try: `streamlit run main.py --server.headless true`

### Installation issues
```bash
# If dependency conflicts:
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 📂 Project Structure

```
LocalLearn-AI/
├── main.py                  # Main Streamlit app
├── requirements.txt         # Dependencies
├── agents/
│   └── tutor_agent.py      # Multi-agent system logic
├── utils/
│   └── audio_utils.py      # TTS functionality
└── README.md               # This file
```

## 🎓 Educational Impact

This app helps students who:
- Are more comfortable in their mother tongue
- Struggle with English-only educational content
- Need relatable, context-specific examples
- Want to hear concepts in familiar terms

**Making science accessible, one local language at a time.**

## 🤝 Contributing

Ideas to extend:
- Add more languages (Assamese, Odia, etc.)
- Improve regional context examples
- Add actual OCR integration
- Create mobile app version
- Add quiz/test features

## 📝 License

Open-source for educational purposes.

## 🙏 Credits

- **AI Framework**: Google ADK (Agent Development Kit)
- **TTS**: Google Text-to-Speech (gTTS)
- **UI**: Streamlit
- **Concept**: Bridging language barriers in education

---

**Made with ❤️ for students learning in their mother tongue**

*LocalLearn - Making science accessible in every language*

**Banner Title**: "LocalLearn – Science in Your Language & Style"
