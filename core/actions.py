import os
import webbrowser

def perform_action(command: str):
    command = command.lower()

    if "open vs code" in command:
        os.system("code .") 
        return "Opening VS Code."
    elif "open jarvis folder" in command:
        path = "/home/rarecode_linux/jarvis-ai"
        os.system(f'code "{path}"')
        return "Opening Jarvis folder."

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "open browser" in command:
        webbrowser.open("https://www.google.com")
        return "Opening browser."

    else:
        return "Sorry, I don't know how to do that yet."
