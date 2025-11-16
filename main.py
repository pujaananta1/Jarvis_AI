import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import random

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

def chat(query):
    # Placeholder: simple echo instead of OpenAI API
    response = f"You said: {query}"
    print(f"Jarvis: {response}")
    say(response)

if __name__ == '__main__':
    say("Jarvis A.I")
    while True:
        query = takeCommand().lower()

        if "open youtube" in query:
            say("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            say("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour}:{minute}")

        elif "exit" in query or "quit" in query:
            say("Goodbye!")
            break

        else:
            chat(query)
