from gtts import gTTS
import streamlit as st
import os
import uuid
import tempfile

# Try to import offline TTS as fallback
try:
    import pyttsx3
    OFFLINE_TTS_AVAILABLE = True
except ImportError:
    OFFLINE_TTS_AVAILABLE = False

LANG_CODES = {
    "Kannada":"kn", "Hindi":"hi", "Tamil":"ta", "Telugu":"te", "Malayalam":"ml",
    "Marathi":"mr", "Gujarati":"gu", "Bengali":"bn", "Punjabi":"pa", "Urdu":"ur",
    "English":"en"
}

def speak_text_offline(text, language="Kannada"):
    """Generate audio using offline TTS (pyttsx3) as fallback."""
    if not OFFLINE_TTS_AVAILABLE:
        return None, None

    try:
        if not text or not text.strip():
            return None, None

        # Create a unique temporary file
        temp_dir = tempfile.gettempdir()
        audio_file = os.path.join(temp_dir, f"tts_offline_{uuid.uuid4().hex}.wav")

        # Initialize offline TTS engine
        engine = pyttsx3.init()

        # Set language/voice if possible (limited support)
        voices = engine.getProperty('voices')
        if language == "English":
            # Try to find English voice
            for voice in voices:
                if 'english' in voice.name.lower() or 'en' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break

        # Generate and save audio
        engine.save_to_file(text, audio_file)
        engine.runAndWait()

        # Read audio bytes
        if os.path.exists(audio_file):
            with open(audio_file, "rb") as f:
                audio_bytes = f.read()
            return audio_bytes, audio_file

    except Exception as e:
        print(f"DEBUG: Offline TTS failed: {str(e)}")

    return None, None

def speak_text(text, language="Kannada"):
    """Generate and return audio data from text using gTTS with offline fallback."""
    try:
        if not text or not text.strip():
            print("DEBUG: No text provided for audio generation")
            return None, None

        lang_code = LANG_CODES.get(language, "en")
        print(f"DEBUG: Generating audio for language: {language} -> {lang_code}")
        print(f"DEBUG: Text length: {len(text)} characters")

        # Create a unique temporary file to avoid conflicts
        temp_dir = tempfile.gettempdir()
        audio_file = os.path.join(temp_dir, f"tts_{uuid.uuid4().hex}.mp3")
        print(f"DEBUG: Audio file path: {audio_file}")

        # Generate TTS
        print("DEBUG: Creating gTTS object...")
        tts = gTTS(text=text, lang=lang_code, slow=False)
        print("DEBUG: Saving audio file...")
        tts.save(audio_file)

        # Verify file was created
        if not os.path.exists(audio_file):
            raise Exception(f"Audio file was not created: {audio_file}")

        file_size = os.path.getsize(audio_file)
        print(f"DEBUG: Audio file size: {file_size} bytes")

        if file_size == 0:
            raise Exception("Audio file is empty")

        # Read audio bytes
        print("DEBUG: Reading audio bytes...")
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()

        print(f"DEBUG: Audio bytes length: {len(audio_bytes)}")
        return audio_bytes, audio_file

    except Exception as e:
        print(f"DEBUG: Exception in speak_text: {str(e)}")
        error_msg = str(e).lower()

        if "429" in error_msg or "too many requests" in error_msg:
            st.warning("⚠️ Google TTS is rate-limited. Trying offline TTS...")
            # Try offline TTS as fallback
            offline_result = speak_text_offline(text, language)
            if offline_result[0]:
                st.info("✅ Using offline TTS (limited language support)")
                return offline_result
            else:
                st.warning("⚠️ Both online and offline TTS failed.")
                st.info("💡 Try refreshing in 5-10 minutes or use shorter text.")
        elif "network" in error_msg or "connection" in error_msg:
            st.warning("⚠️ Network error. Trying offline TTS...")
            offline_result = speak_text_offline(text, language)
            if offline_result[0]:
                st.info("✅ Using offline TTS (English only)")
                return offline_result
            else:
                st.warning("⚠️ No internet and offline TTS not available.")
        else:
            st.error(f"Failed to generate audio: {str(e)}")

        # Return None to indicate failure
        return None, None

def play_audio(audio_bytes):
    """Play audio using HTML audio player."""
    if audio_bytes:
        print(f"DEBUG: Playing audio, bytes length: {len(audio_bytes)}")
        # Create data URL for the audio
        import base64
        audio_base64 = base64.b64encode(audio_bytes).decode()
        print(f"DEBUG: Base64 encoded length: {len(audio_base64)}")

        # HTML audio player with dark theme styling
        audio_html = f"""
        <audio id="tts-audio" controls style="width: 100%; background-color: #1a1a1a; border: 1px solid #444; border-radius: 5px; padding: 5px;">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        <style>
        audio {{
            filter: invert(0.9);
        }}
        audio::-webkit-media-controls-panel {{
            background-color: #1a1a1a !important;
        }}
        audio::-webkit-media-controls-current-time-display,
        audio::-webkit-media-controls-time-remaining-display {{
            color: #ffffff !important;
        }}
        </style>
        """

        st.markdown(audio_html, unsafe_allow_html=True)
        print("DEBUG: Audio player HTML rendered")
        return True
    else:
        print("DEBUG: No audio bytes to play")
        return False
