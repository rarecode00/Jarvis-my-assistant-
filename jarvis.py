from core.speech_out import speak
from core.speech_in import listen_for_speech
from core.actions import perform_action

def main():
    speak("Hello Krishna, I’m online and ready.")
    while True:
        query = listen_for_speech()

        if not query:
            continue

        if "stop" in query or "exit" in query:
            speak("Goodbye Krishna!")
            break

        action = perform_action(query)
        speak(action)

if __name__ == "__main__":
    main()
