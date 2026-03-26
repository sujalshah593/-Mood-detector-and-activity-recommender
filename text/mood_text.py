import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from llama_cpp import Llama   
import torch
import random


print("🔄 Loading emotion model...")
emotion_tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
emotion_model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
print("✅ Emotion model loaded!")


print("🔄 Loading Mistral model...")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

llm = Llama(
    model_path=os.path.join(BASE_DIR, "models", "mistral-7b-instruct-v0.2.Q4_K_M.gguf"),
    n_ctx=2048,
    n_gpu_layers=0,
    verbose=False
)

print("✅ Mistral loaded!")


labels = [
    "admiration","amusement","anger","annoyance","approval","caring",
    "confusion","curiosity","desire","disappointment","disapproval",
    "disgust","embarrassment","excitement","fear","gratitude","grief",
    "joy","love","nervousness","optimism","pride","realization",
    "relief","remorse","sadness","surprise","neutral"
]


def detect_emotion(text):
    inputs = emotion_tokenizer(text, return_tensors="pt", truncation=True)
    outputs = emotion_model(**inputs)
    probs = torch.sigmoid(outputs.logits)[0]

    emotions = []
    for i, p in enumerate(probs):
        if p > 0.4:
            emotions.append(labels[i])

    return emotions if emotions else ["neutral"]



def generate_response(user_input, emotions):
    emotion_text = ", ".join(emotions)

    prompt = f"""<s>[INST]
You are a friendly and supportive chatbot.

User emotion: {emotion_text}
User message: "{user_input}"

Respond naturally like a human in 1-2 lines.
Do NOT give instructions.
[/INST]"""

    output = llm(                          
        prompt,
        max_tokens=120,                   
        temperature=0.8,
        top_p=0.9,
        echo=False                        
    )

    response = output["choices"][0]["text"] 
    return clean_response(response)



def clean_response(text):
    if isinstance(text, bytes):
        text = text.decode("utf-8")

    bad_phrases = [
        "instruction", "user:", "assistant:", "[inst]"
    ]

    text_lower = text.lower()

    for phrase in bad_phrases:
        if phrase in text_lower:
            return fallback_response()

    return text.strip()


def fallback_response():
    return random.choice([
        "I'm here for you. Want to talk about it?",
        "That sounds interesting. Tell me more 😊",
        "I understand. How are you feeling exactly?",
        "Hmm, what's going on in your mind?"
    ])


def analyze_mood_text(text):
    text_lower = text.lower().strip()

    if text_lower in ["hi", "hello", "hey"]:
        return {
            "emotion": ["neutral"],
            "response": random.choice([
                "Hey! 😊 How are you feeling today?",
                "Hello! What's on your mind?",
                "Hi there! Tell me how you're feeling."
            ]),
            "activities": [],
            "message": ""
        }

    if not text_lower:
        return {
            "emotion": ["neutral"],
            "response": "Tell me how you're feeling 😊",
            "activities": [],
            "message": ""
        }

    emotions = detect_emotion(text)
    response = generate_response(text, emotions)

    return {
        "emotion": emotions,
        "response": response,
        "activities": [],
        "message": ""
    }