#!/usr/bin/env python3
"""
Test script to validate Google AI API key
Run this before using the LocalLearn app to ensure your API key works.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

def test_api_key():
    # Load environment variables
    load_dotenv()

    # Check for API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY not found in environment variables")
        print("Please create a .env file with: GOOGLE_API_KEY=your_api_key_here")
        return False

    print(f"✅ Found API key: {api_key[:10]}...{api_key[-5:]}")

    # Validate API key format
    if not api_key.startswith('AIza'):
        print("❌ ERROR: Invalid API key format")
        print("Google AI API keys should start with 'AIza'")
        print(f"Your key starts with: {api_key[:10]}...")
        print("Please get a new API key from: https://makersuite.google.com/app/apikey")
        return False

    print("✅ API key format is valid")

    # Test API key with a simple request
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content("Hello, just testing the API key. Please respond with 'API key works!'")

        if response and hasattr(response, 'text') and response.text:
            print("✅ API key test successful!")
            print(f"Response: {response.text.strip()}")
            return True
        else:
            print("❌ ERROR: API returned empty response")
            return False

    except Exception as e:
        print(f"❌ ERROR: API key validation failed: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you copied the API key correctly")
        print("2. Check if the API key has Gemini API access")
        print("3. Try generating a new API key")
        print("4. Make sure your .env file is in the project root directory")
        return False

if __name__ == "__main__":
    print("🔍 Testing Google AI API Key for LocalLearn...")
    print("=" * 50)

    success = test_api_key()

    print("=" * 50)
    if success:
        print("🎉 Your API key is working! You can now run the LocalLearn app.")
    else:
        print("💥 Please fix the API key issues before running the app.")
        print("Run: streamlit run main.py")
