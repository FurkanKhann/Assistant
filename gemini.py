import google.generativeai as genai
import json

# Configure your Gemini API key
genai.configure(api_key="YOUR API KEY")

def analyze_command(command):
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash")

        # Prompt updated to instruct Gemini to auto-generate message content
        prompt = f"""
You are a smart AI assistant. Analyze the following user command and respond with a JSON object.

Expected JSON format:
{{
  "task_type": "email" | "whatsapp" | "general",
  "recipient": "recipient's email or phone number if applicable",
  "subject": "short subject or title of the message",
  "content": "actual message body based on the context"
}}

If the user does not provide a message body, generate a suitable message using the subject or topic.
ONLY return valid JSON. No extra explanations or markdown formatting.

Command: {command}
"""

        response = model.generate_content(prompt)
        response_text = response.text.strip()

        # Remove markdown formatting if present
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()

        print(f"\n🔍 Gemini raw response:\n{response_text}\n")  # Optional: debug print

        data = json.loads(response_text)

        # Fallback if content is missing or empty
        content = data.get("content", "").strip()
        if not content:
            content = f"This is an auto-generated message regarding '{data.get('subject', 'no subject')}'."

        return {
            "task_type": data.get("task_type", "general"),
            "recipient": data.get("recipient"),
            "subject": data.get("subject", "No Subject"),
            "content": content
        }

    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        return {
            "task_type": "general",
            "recipient": None,
            "subject": "Error",
            "content": "Gemini response was not valid JSON."
        }

    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return {
            "task_type": "general",
            "recipient": None,
            "subject": "Error",
            "content": "Gemini failed to analyze the command."
        }
