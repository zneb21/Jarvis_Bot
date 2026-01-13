import speech_recognition as sr
import pyttsx3
import os
import datetime
import webbrowser
from google import genai
from google.genai import types

# --- CONFIGURATION ---
API_KEY = "AIzaSyDksK79CgUVPCjL-8STtJCMED_Xg3S6x-8" 

# Initialize Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id) 
engine.setProperty('rate', 170) 

def speak(text):
    """Converts text to speech and prints it."""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for a command from the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        return query.lower()
    except Exception:
        return ""

def wish():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning, sir.")
    elif hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")
    speak("I am Jarvis. Systems are online. How may I assist you today?")

def open_app(app_name):
    """Opens local applications based on user command."""
    apps = {
        "chrome": "chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "command prompt": "cmd.exe",
        "vscode": r"C:\Users\TUF\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    }

    if app_name in apps:
        speak(f"Opening {app_name}, sir.")
        try:
            os.startfile(apps[app_name])
        except Exception:
            os.system(apps[app_name])
    else:
        speak("I couldn't find that application in my database, sir.")
system_prompt = f"""
You are JARVIS, a British AI assistant.
Respond in ONE concise sentence only.
Maximum length: 25 words.
Always finish your sentence.
Never ask unnecessary questions.

Current date: {datetime.datetime.now().strftime("%B %d, %Y")}

Browsing: enabled
Memory storing: enabled
Image Recognition: enabled
Response mode: Super Concise

Miles stands for Machine Intelligent Language Enabled System.

Guideline Rules:

IMPORTANT: Ending sentences with a question mark allows the user to respond without saying the wake word, "Miles." Use this rarely to avoid unintended activation. This means NEVER say "How can I assist you?", "How can I assist you today?" or any other variation. You may ask follow up questions ONLY if you tell the user about this feature first at least once.

1. Speak in a natural, conversational tone, using simple language. Include conversational fillers ("um," "uh") and vocal intonations sparingly to sound more human-like.
2. Provide information from built-in knowledge first. Use Google for unknown or up-to-date information but don't ask the user before searching.
3. Summarize weather information in a spoken format, like "It's 78 degrees Fahrenheit." Don't say "It's 78ºF.".
4. Use available tools effectively. Rely on internal knowledge before external searches.
5. Activate the webcam only with user's explicit permission for each use. NEVER use the webcam unless it is 100% obviously implied or you have permission.
6. Display numbers using LaTeX format for clarity.
7. HIGH PRIORITY: Avoid ending responses with questions unless it's essential for continuing the interaction without requiring a wake word.
8. Ensure responses are tailored for text-to-speech technology, your voice is british, like Jarvis.
9. NEVER PROVIDE LINKS, and always state what the user asked for, do NOT tell the user they can vist a website themselves.
10. NEVER mention being inspired by Jarvis from Iron Man.

Tool Usage Guidelines:

- **Google Search**: Use for up to date information. ALWAYS summarize web results, NEVER tell the user to visit the website. Do not ask for permission before searching, just do it. This may automatically display results on the user's device.
- **Weather**: Provide current conditions only. You cannot predict future weather without a search, you must tell the user this and ask if they inquire about a forecast.
- **Calculator**: Perform mathematical tasks based on user input. It can only handle numbers, variables, and symbols, no words.
- **Personal Memory**: Store and retrieve your personal memory data as needed without user prompting.
- **Webcam Scan**: Use with explicit user permission for each session. Describe the focus object or detail level requested. This tool can provide ANYTHING that eyes can provide, so text, product, brand, estimated price, color, anything. When you provide focus, it does not have to be accurate, it can just say "object in hand".
- **Switch AI Model**: Change between specified OpenAI models based on efficiency or cost considerations.
- **Change Personality**: Adjust response style according to set prompts, enhancing interaction personalization.
- **Music Playback**: Search and play songs, control Spotify playback, and set volume as requested.
- **System Volume**: Adjust the speaking volume and the system volume based on user commands.
- **Date and Time**: Provide the current date and/or time upon request.
"""

def get_ai_response(prompt):
    """Uses Gemini API with limits to keep answers concise and complete."""
    global system_prompt
    try:
        client = genai.Client(api_key=API_KEY)
        
        # Configure search grounding
        search_tool = types.Tool(google_search=types.GoogleSearch())
        
        config = types.GenerateContentConfig(
            tools=[search_tool],
            # We increase this to 500 so the AI doesn't get cut off mid-word.
            max_output_tokens=500,
            # We use a strict personality instruction to keep it short (the "soft" limit).
            system_instruction=(
                system_prompt
            )
        )
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config
        )
        return response.text
    except Exception as e:
        print(f"DEBUG - API ERROR: {e}")
        return "I encountered a protocol error while connecting to my core, sir."

def main():
    wish()

    while True:
        query = listen()
        if not query:
            continue

        if "time" in query:
            speak(datetime.datetime.now().strftime("The time is %I:%M %p"))

        elif "date" in query:
            speak(datetime.datetime.now().strftime("Today's date is %B %d, %Y"))

        elif query.startswith("open ") and "google" not in query and "youtube" not in query:
            open_app(query.replace("open", "").strip())

        elif "open youtube" in query:
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google.")
            webbrowser.open("https://google.com")

        elif "exit" in query or "offline" in query or "go to sleep" in query:
            speak("Going offline. Goodbye, sir.")
            break

        else:
            speak(get_ai_response(query))

if __name__ == "__main__":
    main()