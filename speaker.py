import pyttsx3
import threading

# Initialize engine only once
engine = pyttsx3.init()

# Use a lock to prevent race conditions in multi-threaded environments
lock = threading.Lock()

def speaker(text):
    def speak():
        with lock:
            engine.say(text)
            engine.runAndWait()

    threading.Thread(target=speak).start()
