#!/usr/bin/env python3
"""
Test script to check audio generation functionality
"""

import os
from dotenv import load_dotenv
from utils.audio_utils import speak_text, LANG_CODES

def test_audio_generation():
    # Load environment variables
    load_dotenv()

    print("🔍 Testing Audio Generation...")
    print("=" * 50)

    # Test different languages and texts
    test_cases = [
        ("English", "Hello, this is a test of the audio system."),
        ("Hindi", "नमस्ते, यह ऑडियो सिस्टम का परीक्षण है।"),
        ("Kannada", "ನಮಸ್ಕಾರ, ಇದು ಆಡಿಯೋ ಸಿಸ್ಟಮ್ ಪರೀಕ್ಷೆ."),
    ]

    for language, text in test_cases:
        print(f"\n🧪 Testing {language}:")
        print(f"Text: {text[:50]}...")

        try:
            audio_bytes, audio_file = speak_text(text, language)

            if audio_bytes and audio_file:
                print(f"✅ Success! Audio file: {audio_file}")
                print(f"   Audio bytes: {len(audio_bytes)} bytes")
                print(f"   File exists: {os.path.exists(audio_file)}")

                if os.path.exists(audio_file):
                    file_size = os.path.getsize(audio_file)
                    print(f"   File size: {file_size} bytes")

                    # Clean up
                    try:
                        os.remove(audio_file)
                        print("   File cleaned up")
                    except:
                        print("   Could not clean up file")

            else:
                print("❌ Failed: No audio data returned")

        except Exception as e:
            print(f"❌ Error: {str(e)}")

    print("\n" + "=" * 50)
    print("🎵 Audio test completed!")

if __name__ == "__main__":
    test_audio_generation()
