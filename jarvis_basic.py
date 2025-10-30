import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time

# Initialize recognizer and voice engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Helper function for Jarvis to speak
def speak(text):
    print(f"🧠 Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("⏳ Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}")
        return query.lower()
    except Exception as e:
        speak("Sorry, I didn't catch that. Can you repeat?")
        return ""

# Function to handle commands
def process_command(query):
    if "open youtube" in query:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open("https://google.com")

    elif "open vs code" in query:
        speak("Opening Visual Studio Code.")
        # Update path according to your system
        os.system("code")

    elif "time" in query:
        current_time = time.strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "exit" in query or "stop" in query:
        speak("Goodbye Krishna.")
        exit()

    else:
        speak("I’m not sure how to do that yet.")

# Main loop
if __name__ == "__main__":
    speak("Hello Krishna, Jarvis is online.")
    while True:
        query = listen()
        process_command(query)
