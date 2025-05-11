import re

def classifier(text):
    text_lower = text.lower()

    # Regular expression for email detection
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    email_address = email_match.group() if email_match else None

    # Heuristics to identify if the text is related to email
    email_keywords = ["send email", "mail", "write to", "email to", "compose email", "drop a mail"]
    is_email_task = any(keyword in text_lower for keyword in email_keywords) or email_address is not None

    if is_email_task:
        # Try to extract subject: look for "about", "regarding", "with subject" etc.
        subject_match = re.search(r"(about|regarding|subject is|with subject)\s+(.*)", text_lower)
        subject = subject_match.group(2).strip().capitalize() if subject_match else "General Inquiry"
        return {
            "category": "Email",
            "receiver_email": email_address,
            "subject": subject
        }

    # Check for math-related phrases
    math_keywords = ["solve", "calculate", "evaluate", "+", "-", "*", "/", "integral", "derivative", "equation"]
    if any(keyword in text_lower for keyword in math_keywords):
        return {
            "category": "Maths Problem"
        }

    # Check for code-related terms
    code_keywords = ["debug", "function", "error", "loop", "variable", "compile", "syntax", "program"]
    if any(keyword in text_lower for keyword in code_keywords):
        return {
            "category": "Code Help"
        }

    # If nothing matches, treat as a general task
    return {
        "category": "General Task",
        "description": text
    }
