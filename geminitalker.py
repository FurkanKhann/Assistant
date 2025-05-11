import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="YOUR API KEY")  

def talker(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")  
        response = model.generate_content("you have to behave as my assistant and answer to given this"+ prompt+"It should short and concise")

        # Log raw output
        print("🔍 Gemini raw response:")
        print(response.text)

        return response.text or "No response from Gemini."
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "Gemini failed to generate content."
