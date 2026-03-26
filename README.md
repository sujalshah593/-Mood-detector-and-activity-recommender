# 🧠 Mood Detector & Activity Recommender

An AI-powered web app that detects your mood through **face scanning** or **text chat**, and recommends personalized activities based on how you feel.

---

## ✨ Features

- 🎭 **Face Emotion Detection** — Uses your camera to detect emotions in real time using DeepFace AI
- 💬 **Text Chat Bot** — Chat with an AI bot (ChatGPT / local Mistral) that understands your mood
- 🎯 **Activity Recommendations** — Get personalized activity suggestions based on your detected emotion
- 📱 **Mobile-friendly UI** — Clean dark-themed interface with bottom navigation

---

## 🖥️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Face Detection | DeepFace |
| Text Chat | OpenAI GPT / Mistral (local) |
| Frontend | HTML, CSS, JavaScript |
| Emotion Labels | Custom keyword mapping |

---

## 📁 Project Structure

```
ProjectPython/
├── app/
│   └── main.py              # Flask app — routes and API endpoints
├── emotion/
│   └── test_emotion.py      # Face emotion detection using DeepFace
├── recommender/
│   └── activity_map.py      # Emotion → activity suggestions mapping
├── text/
│   └── mood_text.py         # Text-based mood analysis
├── templates/
│   └── index.html           # Frontend UI
├── static/
│   └── style.css            # App styles
├── requirement.txt          # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sujalshah593/-Mood-detector-and-activity-recommender.git
cd -Mood-detector-and-activity-recommender
```

### 2. Install Dependencies

```bash
pip install -r requirement.txt
```

### 3. Set Your OpenAI API Key

```bash
# Windows
set OPENAI_API_KEY=your-api-key-here

# Mac/Linux
export OPENAI_API_KEY=your-api-key-here
```

> Get your API key from: https://platform.openai.com/api-keys

### 4. Run the App

```bash
python app/main.py
```

Then open your browser and go to:
```
http://localhost:5000
```

---

## 📱 How to Use

### Face Scan
1. Click **Face Recognition** on the home screen
2. Allow camera access
3. Click **Scan my face**
4. See your detected emotion + activity suggestions

### Text Chat
1. Click **Text Mood Detector** on the home screen
2. Type how you are feeling (e.g. *"I am feeling stressed"*)
3. Get a friendly response + activity suggestions

---

## 🎯 Supported Emotions & Activities

| Emotion | Example Activities |
|---------|--------------------|
| 😊 Happy | Start your hardest task, Set a new goal, Help someone |
| 😢 Sad | Listen to calming music, Take a walk, Call a friend |
| 😠 Angry | Deep breathing, Write your feelings, Go for a run |
| 😨 Fear / Anxious | Break tasks into steps, Grounding exercise, Meditate |
| 😐 Neutral / Bored | Read something useful, Organize your desk, Learn a skill |
| 😲 Surprise | Reflect, Journal, Stay calm and breathe |
| 🤢 Disgust | Clean your space, Fresh air, Drink water |

---

## ⚙️ Requirements

```
flask
deepface
opencv-python
transformers
torch
openai


## 🔒 Important

- Never share or commit your OpenAI API key publicly
- Use environment variables to keep your key safe

---

## 👨‍💻 Author

**Sujal Shah**
GitHub: [@sujalshah593](https://github.com/sujalshah593)

---

## 📄 License

This project is open source and available for educational use.
