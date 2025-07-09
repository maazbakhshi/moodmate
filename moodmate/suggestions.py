# suggestions.py

import json
from datetime import datetime
from textblob import TextBlob

# --- Load the latest user profile from profile.json ---
def load_profile():
    with open("profile.json", "r") as f:
        profiles = json.load(f)
    return profiles[-1]  # Get the most recent profile (last in the list)


# --- Detect mood from text using TextBlob ---
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    print(polarity)

    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"


# --- Determine time of day: morning, afternoon, or evening ---
def get_time_of_day():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    else:
        return "evening"


# --- Suggest something based on mood + interest + time ---
def suggest_activity(mood, interests, time):
    print(mood, interests, time)
    if mood == "sad" and "Scrolling" in interests and time == "evening":
        return "Try scrolling through your social media accounts. 📱"
    elif mood == "happy" and "Football" in interests and time == "afternoon":
        return "Perfect time for a quick game or run! 🏃"
    elif mood == "neutral" and "reading" in interests:
        return "Pick up a short story to boost your day. 📚"
    else:
        return "Take a short break and breathe. 💨"


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    profile = load_profile()
    interests = profile["interests"]

    entry = input("How are you feeling today? Write a short journal entry:\n")
    mood = detect_mood(entry)
    time = get_time_of_day()

    suggestion = suggest_activity(mood, interests, time)

    print(f"\nYour mood: {mood}")
    print(f"Time of day: {time}")
    print("👉 Suggestion:", suggestion)

