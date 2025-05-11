import pywhatkit
from speaker import speaker

def play_song(song):
    if song:
        speaker(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
    else:
        speaker("Sorry, I didn't catch the song name.")
