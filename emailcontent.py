import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="YOUR API")

def emailgenerator(prompt, receiver):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        prompt_text = (
            f"Write a professional, properly structured email to {receiver} "
            f"about: {prompt}. Format it clearly with:\n"
            f"- Subject line\n"
            f"- A greeting (e.g., Dear Sir/Madam)\n"
            f"- Separate, short paragraphs with line breaks\n"
            f"- A formal closing\n"
            f"- Include the sender’s full name and phone number at the end:\n"
            f"  Name: Furkan Khan\n"
            f"  Phone: +91-9871601543\n"
            f"Ensure it looks like a real professional plain-text email."
        )

        response = model.generate_content(prompt_text)

        # Extract and clean response
        content = response.text.strip() if hasattr(response, 'text') else "No response from Gemini."
        
        # Ensure clean formatting with proper newlines
        formatted_content = "\n".join(line.strip() for line in content.split('\n') if line.strip())

        print("🔍 Gemini formatted email:")
        print(formatted_content)

        return formatted_content

    except Exception as e:
        print(f"⚠️ Error generating email: {e}")
        return "Error generating email."
