import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="API KEY")  # ← replace with your actual API key

def generate_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")  # or gemini-1.5-pro if available
        response = model.generate_content(prompt)

        # Log raw output
        print("🔍 Gemini raw response:")
        print(response.text)

        return response.text or "No response from Gemini."
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "Gemini failed to generate content."
