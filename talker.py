from listener import wait_for_wake_word, listen_for_command
from speaker import speaker
from geminitalker import talker

print("🤖 Assistant is running. Say 'Hello Assistant' to start talking. Say 'assistant off' to stop.\n")

while True:
    if wait_for_wake_word():  # Wait until wake word is heard
        while True:  # Inner loop: take continuous commands
            text = listen_for_command()

            if text is None:
                continue

            if "assistant off" in text.lower():
                print("assistant turned off.")
                speaker("Goodbye! Assistant turned off.")
                exit()

            response = talker(text)
            speaker(response)
