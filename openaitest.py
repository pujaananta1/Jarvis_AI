# openai_wrapper.py

# Load API key from config
from config import apikey

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# Initialize OpenAI client
client = None
if OpenAI:
    client = OpenAI(api_key=apikey)

# Chat history
chat_history = [
    {"role": "system", "content": "You are Jarvis, a helpful AI assistant."}
]

def chat(query):
    """
    Sends query to OpenAI API and returns the response.
    Falls back to offline mode if API not available.
    """
    global chat_history

    chat_history.append({"role": "user", "content": query})

    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=chat_history,
                temperature=0.7,
                max_tokens=200
            )

            answer = response.choices[0].message["content"]
            chat_history.append({"role": "assistant", "content": answer})

            return answer

        except Exception as e:
            return f"OpenAI API error: {e}"

    else:
        # Offline fallback
        answer = f"(Offline mode) You said: {query}"
        chat_history.append({"role": "assistant", "content": answer})
        return answer


def reset_chat():
    """Clears conversation history."""
    global chat_history
    chat_history = [
        {"role": "system", "content": "You are Jarvis, a helpful AI assistant."}
    ]
