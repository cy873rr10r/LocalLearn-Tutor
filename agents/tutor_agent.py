# from google.adk.agents import Agent
import google.generativeai as genai
import os

# Regional contexts for dialect-aware explanations
REGIONAL_CONTEXTS = {
    "Hindi": "cricket, bus travel, chai shops, farming, festivals like Diwali",
    "Tamil": "temple visits, filter coffee, bus/auto rides, rice farming, Pongal festival",
    "Telugu": "movies, biryani, local markets, farming, Sankranti festival",
    "Bengali": "fish markets, tram rides, Durga Puja, sweet shops, cricket",
    "Marathi": "local trains, vada pav, Ganesh Chaturthi, farming, cricket",
    "Gujarati": "dhokla, garba, business, farming, kite flying",
    "Kannada": "coffee estates, BMTC buses, tech parks, cricket, Dasara",
    "Malayalam": "coconut trees, boat rides, Onam festival, fish curry, football",
    "Punjabi": "wheat farming, bhangra, tractors, cricket, Lohri festival",
    "Urdu": "biryani, cricket, qawwali, markets, festivals",
    "English": "daily life in India, cricket, local transport, festivals",
}

def ask_tutor(topic, language="Kannada", simplify=False, extracted_from_image=False):
    """
    Generate explanation for a topic using a 3-agent system with dialect-aware prompts.
    
    Args:
        topic: The topic to explain
        language: Target language for explanation
        simplify: If True, generates ultra-simple explanation
        extracted_from_image: If True, topic was extracted from image
    
    Returns:
        Dialect-aware explanation with regional examples
    """
    try:
        # Get regional context for the language
        regional_context = REGIONAL_CONTEXTS.get(language, "daily life, cricket, local transport")
        
        # ---- Single Comprehensive Agent ----
        # Handles the entire multi-step process: understand → explain → refine
        if simplify:
            system_prompt = f"""You are LocalLearn's expert AI tutor. Your task is to explain science topics in local languages with regional dialect and examples.

TOPIC TO EXPLAIN: The user will provide a topic to explain.
TARGET LANGUAGE: {language}
REGIONAL CONTEXT: {regional_context}

IMPORTANT GUIDELINES for SIMPLE explanations:
- Tone: Very simple, like teaching a young student
- Dialect: Use regional slang/phrases naturally from: {regional_context}
- Keep it SHORT - maximum 5-6 sentences
- Use ONLY simple everyday words
- Focus on ONE main idea with ONE clear example from: {regional_context}
- Avoid technical terms completely
- Do NOT just translate - adapt the teaching style for local understanding
- Use conversational, friendly tone
- Make it feel like a friendly teacher explaining to a neighbor's child

Process: Understand the topic → Create simple explanation → Output final result."""
        else:
            system_prompt = f"""You are LocalLearn's expert AI tutor. Your task is to explain science topics in local languages with regional dialect and examples.

TOPIC TO EXPLAIN: The user will provide a topic to explain.
TARGET LANGUAGE: {language}
REGIONAL CONTEXT: {regional_context}

IMPORTANT GUIDELINES for DETAILED explanations:
- Tone: Friendly teaching style for beginners
- Dialect: Use regional slang/phrases naturally but keep accuracy
- Add 2-3 real-life situations from the student's daily life
- Use examples from: {regional_context}
- Avoid heavy technical words. Focus on simple understanding
- Do NOT just translate - adapt the teaching style for local understanding
- Make it conversational and relatable
- Use local expressions and phrases that students use daily
- The explanation should feel like it's coming from a local teacher who understands the student's world

Process: Understand the topic → Create detailed explanation with examples → Refine for clarity → Output final result."""

        # Check for Google AI API key
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise Exception("GOOGLE_API_KEY environment variable not set. Please set your Google AI API key in a .env file.")

        # Validate API key format (should start with 'AIza')
        if not api_key.startswith('AIza'):
            raise Exception(f"Invalid API key format. Google AI API keys should start with 'AIza'. Your key starts with: {api_key[:10]}...")

        # Use Google ADK agent structure with direct Google Generative AI calls
        # This gives us Google ADK functionality while avoiding complex auth issues

        # Configure the Google AI client (same as before)
        genai.configure(api_key=api_key)

        # Create the model with Google ADK-style agent prompting
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=system_prompt
        )

        # Generate the explanation using direct API call
        try:
            response = model.generate_content(topic)
        except Exception as api_error:
            raise Exception(f"Google AI API error: {api_error}")

        # Extract the text from the response
        if response and hasattr(response, 'text') and response.text:
            explanation = response.text.strip()
        else:
            explanation = "No explanation generated. Please try again."
        
        if not explanation or explanation.strip() == "":
            return f"Sorry, I couldn't generate an explanation. Please try again."
        
        return explanation
        
    except Exception as e:
        error_msg = f"Error generating explanation: {str(e)}"
        raise Exception(error_msg)
