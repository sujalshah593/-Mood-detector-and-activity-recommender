import random

activity_map = {
    "happy": [
        "Start your hardest task",
        "Work on your main goal for 25 minutes",
        "Plan your day clearly",
        "Share your good mood with someone you love",
        "Start a creative project you've been putting off",
        "Write down 3 things you're grateful for today",
        "Help someone who might need it",
        "Try a new hobby or skill",
        "Go for a run or workout session",
        "Organize something that's been messy for a while",
        "Read a book you've been wanting to start",
        "Cook or bake something new",
        "Reach out to an old friend",
        "Set a new goal for this week",
        "Watch an inspiring documentary or TED talk",
        "Explore a new place in your city",
        "Start journaling about your positive experiences",
        "Do something kind for a stranger"
    ],
    "sad": [
        "Listen to calming music",
        "Take a short walk outside",
        "Call a close friend",
        "Write down your feelings in a journal",
        "Watch your favorite comfort movie",
        "Make yourself a warm drink like tea or hot chocolate",
        "Do gentle yoga or light stretching",
        "Look at happy photos or memories",
        "Cuddle with a pet if you have one",
        "Take a warm shower or bath",
        "Read an uplifting book or story",
        "Step outside and get some fresh air",
        "Do a simple creative activity like drawing or coloring",
        "Listen to a motivational podcast",
        "Cook or order your favorite comfort food",
        "Reach out to a family member",
        "Watch funny videos or memes to lighten your mood",
        "Try a short guided meditation",
        "Volunteer or help someone — it can lift your spirits",
        "Sleep early and rest well tonight"
    ],
    "angry": [
        "Take 5 deep breaths",
        "Do light stretching",
        "Write down what is bothering you",
        "Go for a brisk walk or run",
        "Punch a pillow or scream into it",
        "Count slowly from 1 to 20",
        "Listen to calming or instrumental music",
        "Drink a glass of cold water",
        "Step away from the situation for 10 minutes",
        "Do an intense workout to release energy",
        "Write a letter (that you won't send) about your anger",
        "Talk to someone you trust about it",
        "Try box breathing — inhale 4s, hold 4s, exhale 4s",
        "Clean or organize your room to channel the energy",
        "Play a sport or physically active game",
        "Draw or paint your emotions out",
        "Do progressive muscle relaxation",
        "Watch something funny to shift your mood"
    ],
    "fear": [
        "Break your task into small steps",
        "Do grounding breathing exercise",
        "Talk to someone you trust",
        "Write down exactly what you are afraid of",
        "Challenge the fear — ask: what is the worst that can happen?",
        "Do the 5-4-3-2-1 grounding technique",
        "Listen to calming music or nature sounds",
        "Remind yourself of a time you overcame something hard",
        "Take a slow walk in nature",
        "Watch a comforting or familiar show",
        "Practice deep belly breathing for 5 minutes",
        "Call or text a supportive friend or family member",
        "Do light yoga or stretching",
        "Write down 3 things you can control right now",
        "Take one small action toward what scares you",
        "Limit news or social media if it's causing anxiety",
        "Try a guided meditation for anxiety on YouTube",
        "Make a cup of herbal tea and sit quietly"
    ],
    "surprise": [
        "Take a moment to reflect",
        "Write down your thoughts",
        "Stay calm and think clearly",
        "Give yourself a few minutes before reacting",
        "Talk to someone about what surprised you",
        "Journal about how the surprise made you feel",
        "Take a short walk to process your thoughts",
        "Do deep breathing to settle your mind",
        "Look at the situation from a different angle",
        "Make a pros and cons list if a decision is involved",
        "Be curious — explore the unexpected thing further",
        "Share the surprise with a close friend",
        "Remind yourself that change can lead to good things",
        "Do a quick mindfulness exercise to stay grounded",
        "Watch or read something calming to reset"
    ],
    "disgust": [
        "Clean your workspace",
        "Drink water and refresh yourself",
        "Take a small break",
        "Step outside for fresh air",
        "Wash your face and hands to feel refreshed",
        "Change your environment — move to a different room",
        "Listen to pleasant or uplifting music",
        "Do light stretching to reset your body",
        "Write about what triggered the feeling",
        "Declutter a small area around you",
        "Eat something fresh and healthy",
        "Watch something light-hearted or funny",
        "Practice mindful breathing for 3 minutes",
        "Talk to someone about what you experienced",
        "Do something creative to shift your focus"
    ],
    "neutral": [
        "Do a small productive task",
        "Organize your desk",
        "Read something useful",
        "Make a to-do list for the day",
        "Learn something new for 15 minutes",
        "Go for a casual walk",
        "Listen to a podcast on a topic you like",
        "Try a new recipe or snack",
        "Do a quick 10-minute workout",
        "Write in a journal about your day",
        "Watch a documentary on something interesting",
        "Reach out to a friend you haven't talked to in a while",
        "Declutter one small area of your space",
        "Practice a skill you want to improve",
        "Spend 10 minutes in silence or meditation",
        "Sketch, doodle, or do something creative",
        "Plan something fun for the upcoming weekend",
        "Do a random act of kindness today"
    ]
}


def get_activities_for_emotion(emotion):
    emotion = emotion.lower()

    if emotion not in activity_map:
        return {
            "response": "Take a mindful pause.",
            "activities": ["Relax for a moment"],
            "message": "Couldn't detect emotion clearly."
        }

    activities = activity_map[emotion]

    return {
        "response": random.choice(activities),
        "activities": activities,
        "message": f"You seem {emotion}. Here are some suggestions."
    }