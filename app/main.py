from flask import Flask, render_template, request, jsonify
import sys, os, random

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from emotion.test_emotion import analyze_frame_base64, load_models
from recommender.activity_map import get_activities_for_emotion
from llama_cpp import Llama

app = Flask(__name__,
    template_folder='../templates',
    static_folder='../static'
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

llm = Llama(
    model_path=os.path.join(BASE_DIR, "models", "mistral-7b-instruct-v0.2.Q4_K_M.gguf"),
    n_ctx=2048,
    n_gpu_layers=0,
    verbose=False
)

print("Loading face models...")
load_models()
print("Ready!")



keyword_emotion_map = {
    "happy": "happy",
    "excited": "happy",
    "great": "happy",
    "good": "happy",
    "joy": "happy",

    "sad": "sad",
    "depressed": "sad",
    "crying": "sad",
    "unhappy": "sad",
    "low": "sad",
    "lonely": "sad",
    "grief": "sad",

    "angry": "angry",
    "frustrated": "angry",
    "mad": "angry",
    "irritated": "angry",
    "annoyed": "angry",

    "scared": "fear",
    "afraid": "fear",
    "anxious": "fear",
    "nervous": "fear",
    "fear": "fear",
    "worried": "fear",
    "stress": "fear",
    "stressed": "fear",

    "bored": "neutral",
    "tired": "neutral",
    "okay": "neutral",
    "fine": "neutral",
    "meh": "neutral",
    "scrolling": "neutral",
    "reels": "neutral",
    "nothing to do": "neutral",

    "disgusted": "disgust",
    "sick": "disgust",
    "gross": "disgust",

    "surprised": "surprise",
    "shocked": "surprise",
    "unexpected": "surprise"
}

def detect_emotion_from_text(text):
    text_lower = text.lower()
    for keyword, emotion in keyword_emotion_map.items():
        if keyword in text_lower:
            return emotion
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze-face', methods=['POST'])
def analyze_face():
    try:
        data = request.json
        result = analyze_frame_base64(data.get('image'))
        if 'error' not in result:
            recs = get_activities_for_emotion(result['dominant_emotion'])
            result['response'] = recs['response']
            result['activities'] = recs['activities']
            result['message'] = recs['message']
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    try:
        data = request.json
        user_input = data.get('text', '').strip()

        if not user_input:
            return jsonify({
                "response": "Say something, I'm listening 😊",
                "activities": [],
                "message": ""
            })

        detected_emotion = detect_emotion_from_text(user_input)

        activities = []
        message = ""
        if detected_emotion:
            recs = get_activities_for_emotion(detected_emotion)
            activities = recs['activities']
            message = recs['message']

        prompt = f"""<s>[INST]
You are a friendly and supportive chatbot.
User message: "{user_input}"
Respond naturally like a human in 1-2 lines. Do NOT give instructions.
[/INST]"""

        output = llm(
            prompt,
            max_tokens=120,
            temperature=0.8,
            top_p=0.9,
            echo=False
        )
        response = output["choices"][0]["text"].strip()

        if not response:
            response = random.choice([
                "I'm here for you. Want to talk about it?",
                "That sounds tough. Tell me more 😊",
                "I understand. How are you feeling exactly?"
            ])

        return jsonify({
            "response": response,
            "activities": activities,
            "message": message
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=False, port=5000)

