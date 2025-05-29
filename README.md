# 🤖 Smart Assistant (Voice + UI Based AI Assistant)

A smart desktop assistant powered by Google Gemini AI, Streamlit, and voice commands. It can send professional emails, control system utilities, play music, take notes, run reminders, and more—all through a voice-controlled or web-based dashboard.

---

## 📂 Features

- 🎙️ Voice activation using wake word: `"hello assistant"`
- 🧠 Natural language understanding using Gemini API
- 📧 Generate and send professional emails
- 🎵 Play songs by name
- 📂 Open local folders and files (Desktop/Downloads)
- 🌐 Launch popular websites (Google, YouTube, LeetCode)
- 📸 Take and save screenshots
- 📝 Quick note-taking with timestamps
- ⏰ Countdown reminders with voice alerts
- 🔇 System control: mute, shutdown, restart, lock, etc.
- 💻 Web-based dashboard with [Streamlit](https://streamlit.io/)

---

## 🛠️ Tech Stack

- Python
- Google Gemini API (Generative AI)
- Streamlit (Web UI)
- pyttsx3 (Text-to-Speech)
- SpeechRecognition (Voice recognition)
- smtplib (Email sending)
- pyautogui (Screenshot and automation)
- OS utilities and file system

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/FurkanKhann/Assistant.git
cd Assistant
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Update your Google Gemini API key in:
- `emailcontent.py`
- `gemini.py`
- `gemini_generator.py`
- `geminitalker.py`

Also, set up your email credentials in `emailer.py`:

```python
from_email = "your-email@gmail.com"
app_password = "your-app-password"
```

> ⚠️ **Do not commit your credentials.** Use environment variables in production.

---

## 🧠 Usage

### Web Interface (Streamlit)

```bash
streamlit run iot.py
```

### Voice Interface

```bash
python listener.py
```

Say **"hello assistant"** to activate the assistant.

---

## 🔐 Security Notice

- Avoid hardcoding sensitive information.
- For production, use `.env` files and `os.environ` to manage API keys and passwords securely.

---

## 📁 Project Structure

```
├── classifier.py           # Task classification logic
├── emailcontent.py         # Gemini-based email generator
├── emailer.py              # Email sending logic
├── gemini.py               # Command analyzer (Gemini)
├── gemini_generator.py     # Gemini content generation utility
├── geminitalker.py         # Gemini assistant responses
├── iot.py                  # Streamlit UI
├── listener.py             # Voice recognition listener
├── requirements.txt
```

---

## ✨ Acknowledgments

- [Google Gemini](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)

---

## 📬 Contact

**Developer:** Furkan Khan  
**Phone:** +91-9871601543  
**Email:** khanfurkan575@gmail.com
