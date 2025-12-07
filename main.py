import streamlit as st
import os
from dotenv import load_dotenv
from agents.tutor_agent import ask_tutor
from utils.audio_utils import speak_text, play_audio
from PIL import Image

# Load environment variables
load_dotenv()

# Initialize theme in session state
if 'dark_theme' not in st.session_state:
    st.session_state.dark_theme = True

# Configure page with dark theme
st.set_page_config(
    page_title="LocalLearn - Science in Your Language & Style",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark Theme UI
st.markdown("""
    <style>
    /* Overall dark theme */
    .stApp {
        background-color: #0a0a0a;
        color: #ffffff;
    }

    /* Main content area */
    .main .block-container {
        background-color: #0a0a0a;
        color: #ffffff;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #1a1a1a;
        color: #ffffff;
    }

    /* Input fields */
    .stTextInput > div > div > input {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
        border: 1px solid #444444 !important;
    }

    /* Select boxes */
    .stSelectbox > div > div > div {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #667eea !important;
        color: #ffffff !important;
        border: none !important;
    }

    .stButton > button:hover {
        background-color: #764ba2 !important;
        color: #ffffff !important;
    }

    /* Main banner with dark theme gradient */
    .main-banner {
        background: linear-gradient(135deg, #2a2a2a 0%, #4a4a4a 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 1px solid #555555;
    }
    .main-banner h1 {
        color: #ffffff;
        margin: 0;
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    .main-banner p {
        color: #cccccc;
        margin: 5px 0 0 0;
        font-size: 1.2em;
    }

    /* Output box for explanations */
    .output-box {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin-top: 20px;
        font-size: 1.1em;
        line-height: 1.6;
        color: #ffffff !important;
        white-space: pre-wrap;
        word-wrap: break-word;
        border: 1px solid #333333;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    /* Slider styling */
    .stSlider > div > div > div {
        background-color: #2a2a2a !important;
    }

    /* Headers and text */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }

    /* Regular text */
    p, span, div {
        color: #cccccc;
    }

    /* Success messages */
    .stSuccess {
        background-color: #1a4a1a !important;
        color: #90EE90 !important;
    }

    /* Warning messages */
    .stWarning {
        background-color: #4a4a1a !important;
        color: #FFFFE0 !important;
    }

    /* Error messages */
    .stError {
        background-color: #4a1a1a !important;
        color: #FFB6C1 !important;
    }

    /* Info messages */
    .stInfo {
        background-color: #1a4a4a !important;
        color: #87CEEB !important;
    }

    /* Footer */
    .footer-text {
        color: #888888 !important;
    }

    /* Form labels and other text */
    label, .stMarkdown, .stText {
        color: #ffffff !important;
    }

    /* Radio buttons and checkboxes */
    .stRadio > div, .stCheckbox > div {
        color: #ffffff !important;
    }

    /* Table styling */
    .dataframe {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
    }

    /* Code blocks */
    code {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
    }

    /* Links */
    a {
        color: #667eea !important;
    }

    /* Horizontal rules */
    hr {
        border-color: #444444 !important;
    }

    /* Card-like elements */
    .stCard {
        background-color: #1a1a1a !important;
        border: 1px solid #333333 !important;
        border-radius: 10px !important;
    }

    /* Metric boxes */
    .metric-container {
        background-color: #1a1a1a !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }

    /* Smooth transitions */
    * {
        transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Banner
st.markdown("""
    <div class="main-banner">
        <h1>🌍 LocalLearn – Science in Your Language & Style</h1>
        <p>Learn any topic in your local language with real-life examples</p>
    </div>
""", unsafe_allow_html=True)

st.caption("Powered by Google Gemini AI | Intelligent Local Language Explanations")

# Initialize session state
if 'explanation' not in st.session_state:
    st.session_state.explanation = ""
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = ""
if 'current_language' not in st.session_state:
    st.session_state.current_language = "Hindi"
if 'simplified' not in st.session_state:
    st.session_state.simplified = False

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📚 What do you want to learn?")
    topic = st.text_input(
        "Enter any topic:",
        placeholder="e.g., Newton's First Law, Photosynthesis, Gravity...",
        help="Type any science or educational topic you want to understand"
    )
    
    # Optional: Image upload
    st.markdown("---")
    st.markdown("**📸 Or upload a textbook photo (optional)**")
    uploaded_file = st.file_uploader(
        "Upload image of textbook page",
        type=['png', 'jpg', 'jpeg'],
        help="Upload a photo - you can then type the topic name"
    )
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Textbook Image", use_column_width=True)
        st.info("📝 Please type the topic name from the image above")

with col2:
    st.subheader("🗣️ Select Your Language")
    language = st.selectbox(
        "Choose your preferred language:",
        ["Hindi", "Tamil", "Telugu", "Bengali", "Marathi", "Gujarati", 
         "Kannada", "Malayalam", "Punjabi", "Urdu", "English"],
        help="The explanation will use your local dialect and examples"
    )
    st.session_state.current_language = language

# Action buttons
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    explain_btn = st.button("🎯 Explain", use_container_width=True)

with col_btn2:
    simpler_btn = st.button("🔍 Make Even Simpler", use_container_width=True, 
                            disabled=not st.session_state.current_topic)

with col_btn3:
    clear_btn = st.button("🔄 Clear", use_container_width=True)

# Handle button clicks
if explain_btn:
    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic!")
    else:
        try:
            with st.spinner(f"🤔 Generating explanation in {language}..."):
                explanation = ask_tutor(topic, language, simplify=False)
            st.session_state.explanation = explanation
            st.session_state.current_topic = topic
            st.session_state.simplified = False
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please try again or check your connection.")

if simpler_btn and st.session_state.current_topic:
    try:
        with st.spinner(f"✨ Making it even simpler..."):
            explanation = ask_tutor(st.session_state.current_topic, language, simplify=True)
        st.session_state.explanation = explanation
        st.session_state.simplified = True
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

if clear_btn:
    st.session_state.explanation = ""
    st.session_state.current_topic = ""
    st.session_state.simplified = False
    st.rerun()

# Display output
if st.session_state.explanation:
    st.markdown("---")
    st.subheader("📖 Explanation")
    
    # Display explanation
    # Clean and format the explanation text
    explanation_text = st.session_state.explanation.replace('\n', '<br>').replace('  ', '&nbsp;&nbsp;')
    st.markdown(f'<div class="output-box">{explanation_text}</div>',
                unsafe_allow_html=True)
    
    # Audio player (automatic generation)
    st.markdown("### 🔊 Listen to Explanation")

    # Automatically generate and play audio when explanation changes
    try:
        if st.session_state.get('last_explanation') != st.session_state.explanation:
            st.info("🎵 Generating audio...")

            # Prepare text for TTS (limit length and clean)
            tts_text = st.session_state.explanation[:2000]  # Limit to 2000 chars for gTTS
            tts_text = tts_text.replace('\n', ' ').replace('\r', ' ')  # Remove line breaks

            # Generate new audio
            audio_bytes, audio_file = speak_text(
                tts_text,
                st.session_state.current_language
            )
            if audio_bytes:
                st.session_state.audio_bytes = audio_bytes
                st.session_state.audio_file = audio_file
                st.session_state.last_explanation = st.session_state.explanation
                st.success("✅ Audio generated successfully!")
            else:
                st.warning("⚠️ Audio generation failed. This may be due to rate limiting.")
                st.info("🔄 Try again in a few minutes or use shorter text.")

        # Play audio at normal speed
        if 'audio_bytes' in st.session_state:
            play_audio(st.session_state.audio_bytes)

    except Exception as e:
        st.error(f"❌ Audio generation failed: {str(e)}")
        st.info("💡 Try checking your internet connection or try a shorter text.")

    # Cleanup audio file when session ends or explanation changes
    if 'audio_file' in st.session_state and st.session_state.get('last_explanation') != st.session_state.explanation:
        try:
            import os
            if os.path.exists(st.session_state.audio_file):
                os.remove(st.session_state.audio_file)
        except:
            pass  # Ignore cleanup errors
    
    # Additional info
    if st.session_state.simplified:
        st.success("✅ This is the simplified version")
    else:
        st.info("💡 Click 'Make Even Simpler' for an easier explanation")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888888; padding: 20px;' class='footer-text'>
        <p>💡 <strong>LocalLearn</strong> - Making science accessible in every language</p>
        <p style='font-size: 0.9em;'>Powered by Google ADK Agent Architecture</p>
    </div>
""", unsafe_allow_html=True)
