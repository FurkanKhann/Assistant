import os
import streamlit as st
import webbrowser
import pyttsx3
import time
import datetime
import requests
import pyautogui
from emailcontent import emailgenerator
from emailer import send_email
from song import play_song

st.set_page_config(page_title="Smart Assistant", layout="centered")
st.title("🤖 Smart Assistant Dashboard")

# Initialize speaker
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Session state for assistant status
if "assistant_on" not in st.session_state:
    st.session_state.assistant_on = False

# Toggle assistant state
col1, col2 = st.columns(2)
with col1:
    if st.button("🟢 Assistant On"):
        st.session_state.assistant_on = True
with col2:
    if st.button("🔴 Assistant Off"):
        st.session_state.assistant_on = False
        st.info("Assistant turned off.")

# Show features if assistant is on
if st.session_state.assistant_on:
    st.subheader("✨ Select a Function")

    # --- SEND EMAIL ---
    with st.expander("📧 Send Email"):
        with st.form("email_form"):
            subject = st.text_input("Enter Email Subject")
            receiver = st.text_input("Enter Receiver Email")
            submitted = st.form_submit_button("Send Email")
            if submitted:
                if subject and receiver:
                    content = emailgenerator(subject, receiver)
                    send_email(receiver, subject, content)
                    st.success("✅ Email sent successfully.")
                else:
                    st.warning("⚠️ Please enter both subject and receiver email.")

    # --- PLAY SONG ---
    with st.expander("🎵 Play Something"):
        with st.form("music_form"):
            song_name = st.text_input("Enter Song Name")
            play = st.form_submit_button("Play Song")
            if play:
                if song_name:
                    play_song(song_name)
                    st.success(f"🎶 Playing {song_name}")
                else:
                    st.warning("⚠️ Please enter a song name.")

    # --- OPEN FOLDER ---
    with st.expander("📂 Open Folder - Desktop or Downloads"):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        selected_folder = st.radio("Select Folder", ("Desktop", "Downloads"))
        folder_path = desktop_path if selected_folder == "Desktop" else downloads_path
        if os.path.exists(folder_path):
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            st.write("Files found:", files)
            selected_file = st.selectbox("Select a file to open", files)
            if selected_file:
                if st.button(f"Open {selected_file}"):
                    os.startfile(os.path.join(folder_path, selected_file))
                    st.success(f"Opening {selected_file}...")

    # --- SYSTEM CONTROLS ---
    if st.button("🌐 Open Google"):
        webbrowser.open("https://www.google.com")
        st.info("Opening Google")

    if st.button("📺 Open YouTube"):
        webbrowser.open("https://www.youtube.com")
        st.info("Opening YouTube")

    if st.button("🟢📱 Open WhatsApp"):
        os.system("start whatsapp:")
        st.success("WhatsApp opened")

    if st.button("🔴📱 Close WhatsApp"):
        os.system("taskkill /f /im WhatsApp.exe")
        st.success("WhatsApp closed")

    if st.button("📷 Open Camera"):
        os.system("start microsoft.windows.camera:")
        st.success("Camera opened")

    if st.button("📴 Close Camera"):
        os.system("taskkill /f /im WindowsCamera.exe")
        st.success("Camera closed")

    if st.button("❌ Close Browser"):
        os.system("taskkill /im chrome.exe /f")
        st.success("Browser closed")

    if st.button("⛔ Shutdown"):
        os.system("shutdown /s /t 5")
        st.warning("System will shut down in 5 seconds.")

    if st.button("🔄 Restart"):
        os.system("shutdown /r /t 5")
        st.warning("System will restart in 5 seconds.")

    if st.button("🔇 Mute System"):
        os.system("nircmd.exe mutesysvolume 1")
        st.info("System muted.")

    if st.button("🧠💻 Open LeetCode"):
        webbrowser.open("https://www.leetcode.com")
        st.info("Opening LeetCode")

    # --- NEW FEATURES ---
    with st.expander("⏰ Set Reminder (Countdown)"):
        minutes = st.number_input("Remind me after (minutes):", min_value=1, max_value=120)
        msg = st.text_input("Reminder message")
        if st.button("Start Reminder"):
            st.success(f"⏳ Reminder set for {minutes} minutes.")
            time.sleep(minutes * 60)
            speak(msg or "Time's up!")

    with st.expander("📝 Quick Note Taker"):
        note = st.text_area("Write your note:")
        if st.button("Save Note"):
            with open("quick_notes.txt", "a") as f:
                f.write(f"{datetime.datetime.now()}: {note}\n")
            st.success("📝 Note saved.")

    with st.expander("📸 Screenshot"):
        if st.button("Take Screenshot"):
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{int(time.time())}.png"
            screenshot.save(filename)
            st.success(f"📸 Screenshot saved as {filename}")

   

    if st.button("🔐 Lock Screen"):
        os.system("rundll32.exe user32.dll,LockWorkStation")
        st.success("🔒 Screen locked.")
