# this is used to hear the user voice
# and convert it to text
import speech_recognition as sr

r = sr.Recognizer()

def listen_for_speech():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        print("⏳ Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}")
        return query.lower()

    except sr.UnknownValueError:
        print("❌ Sorry, I couldn’t understand that.")
    except sr.RequestError:
        print("⚠️ Could not connect to the recognition service.")
    except Exception as e:
        print(f"❌ Error: {e}")

    return ""

