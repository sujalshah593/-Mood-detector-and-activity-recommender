
# 🧠 Mood Detector & Activity Recommender

An AI-powered web app that detects your mood through **face scanning** or **text chat**, and recommends personalized activities based on how you feel.

---

## 👨‍💻 Authors

**Sujal Shah**
GitHub: [@sujalshah593](https://github.com/sujalshah593)

**Nidhi Chaudhary**
GitHub: [@nidhii133](https://github.com/nidhii133)

---

## ✨ Features

- 🎭 **Face Emotion Detection** — Uses your camera to detect emotions in real time using DeepFace AI
- 💬 **Text Chat Bot** — Chat with a local AI bot powered by **Mistral via Ollama** that understands your mood
- 🎯 **Activity Recommendations** — Get personalized activity suggestions based on your detected emotion
- 📱 **Mobile-friendly UI** — Clean dark-themed interface with bottom navigation
- 🔒 **100% Local & Private** — No API keys required; everything runs on your machine

---

## 🖥️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Face Detection | DeepFace |
| Emotion Classification | `SamLowe/roberta-base-go_emotions` (HuggingFace Transformers) |
| Text Chat (LLM) | Mistral 7B via **Ollama** (local, no API key needed) |
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
│   └── mood_text.py         # Text-based mood analysis (Transformers + Mistral)
├── models/
│   └── mistral-7b-instruct-v0.2.Q4_K_M.gguf  # Local Mistral model file
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

### 3. Install Ollama & Download Mistral

This project uses **Ollama** to run Mistral locally — no OpenAI API key needed.

**Step 1 — Install Ollama:**
> Download from [https://ollama.com/download](https://ollama.com/download) and install for your OS.

**Step 2 — Pull the Mistral model:**
```bash
ollama pull mistral
```

**Step 3 — Make sure Ollama is running:**
```bash
ollama serve
```
> Ollama runs in the background on `http://localhost:11434` by default.

**Alternative — GGUF file (llama-cpp-python):**
If you prefer to run the model directly from a `.gguf` file without Ollama, place the model at:
```
models/mistral-7b-instruct-v0.2.Q4_K_M.gguf
```
> Download from: [https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

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

and many more activities
---

## ⚙️ Requirements

```
flask
deepface
opencv-python
transformers
torch
llama-cpp-python
```

> Install all at once:
> ```bash
> pip install -r requirement.txt
> ```

---

## 🔒 Privacy & Security

- ✅ **No API keys required** — Mistral runs fully locally via Ollama
- ✅ **No data sent to external servers** — all processing happens on your machine
- ✅ **Camera feed is never stored** — face scan is processed in memory only
- ⚠️ Do **not** commit your model files (`.gguf`) to GitHub — add them to `.gitignore`

---

## 🛠️ Troubleshooting

| Issue | Fix |
|-------|-----|
| `ollama: command not found` | Install Ollama from [ollama.com](https://ollama.com/download) |
| Model not responding | Run `ollama serve` in a separate terminal |
| DeepFace errors on first run | It auto-downloads model weights — wait for it to finish |
| Camera not detected | Check browser permissions and try a different browser |
| `llama_cpp` import error | Run `pip install llama-cpp-python --force-reinstall` |

---

## 📄 License

This project is open source and available for educational use.
