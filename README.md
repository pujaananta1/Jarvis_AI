Jarvis AI (Voice Assistant)

A Python-based voice assistant that uses Speech Recognition, Text-to-Speech, and the OpenAI API to interact with users, open websites, tell the time, and answer general queries.

🚀 Features

🎤 Voice Recognition using speech_recognition

🔊 Text-to-Speech using pyttsx3

🌐 Opens websites like YouTube & Google

⏰ Tells current time

🤖 AI chat responses using OpenAI GPT-4o / GPT-4o-mini

🧠 Maintains conversation history

🛑 Easy exit commands ("exit", "quit")

🧩 Clean file structure with openai_wrapper.py and config.py

▶️ Usage

Run the assistant:

python main.py

Available Commands:
Command	Action
open youtube	Opens YouTube
open google	Opens Google
what is the time	Speaks current time
any question	Jarvis answers using ChatGPT
exit / quit	Stops the program

Jarvis listens, processes your speech, and responds with voice output.

📦 Requirements

Add this to requirements.txt:

speechrecognition
pyttsx3
pyaudio
openai
