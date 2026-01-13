# JARVIS Bot 🎙️🤖

JARVIS is a locally running Python voice assistant built for learning and experimentation, capable of understanding spoken commands, responding with speech, and performing basic system tasks.

## 🚀 Features

* Wake-word activated voice interaction
* Speech recognition via microphone input
* British text-to-speech voice output
* Opens local applications (Chrome, Notepad, Calculator, VS Code)
* Provides current date and time
* AI-powered conversational responses using Google Gemini
* Secure API key handling through environment variables

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* pyttsx3 (Text-to-Speech)
* Google Gemini API
* Git & GitHub

## 📦 Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/jarvis-project.git
   ```
2. Navigate to the project directory:

   ```
   cd jarvis-project
   ```
3. (Optional but recommended) Create a virtual environment.
4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
5. Set your Gemini API key as an environment variable:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## ▶️ Usage

Run the assistant with:

```
python jarvis.py
```

Say the wake word **“Jarvis”**, then issue a command, for example:

* “Jarvis, what time is it”
* “Jarvis, open calculator”
* “Jarvis, explain machine learning”

## 📁 Project Structure

```
Jarvis Project/
│── jarvis.py
│── requirements.txt
│── .gitignore
│── README.md
```

## 🔒 Security Notes

* API keys are **not** stored in the repository.
* Virtual environments and system files are excluded via `.gitignore`.

## 🎯 Purpose

This project was created to practice Python, voice interfaces, API integration, and version control using Git and GitHub.

## 👤 Author

**Zneb Delariman**

---

## ✅ Final Step (Push to GitHub)

After saving the file:

```powershell
git add README.md
git commit -m "Improve README for portfolio"
git push
```


Just tell me what’s next 👌
