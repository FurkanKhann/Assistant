import speech_recognition as sr

recognizer = sr.Recognizer()

def wait_for_wake_word(wake_word="hello assistant"):
    print(f"System is running... Say '{wake_word}' to activate.")
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening for wake word...")

            try:
                audio = recognizer.listen(source)
                trigger_text = recognizer.recognize_google(audio).lower()
                print("Heard:", trigger_text)

                if wake_word in trigger_text:
                    print("✅ Wake word detected.")
                    return True

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"🔴 API Error: {e}")
                return None

def listen_for_command():
    with sr.Microphone() as command_source:
        recognizer.adjust_for_ambient_noise(command_source, duration=0.5)
        print("🎙️ Listening for your command...")
        try:
            audio_cmd = recognizer.listen(command_source)
            command_text = recognizer.recognize_google(audio_cmd)
            print("🗣️ You said:", command_text)
            return command_text
        except sr.UnknownValueError:
            print("❓ Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"🔴 API Error: {e}")
            return None
