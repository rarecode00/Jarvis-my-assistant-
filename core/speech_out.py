import pyttsx3

# initilize the engine
engine = pyttsx3.init();

# speak the text
def speak(text: str):
    if not text:
        return
    engine.say(text)
    engine.runAndWait();