# utils/mood_utils.py

from textblob import TextBlob

def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Classify mood based on polarity score
    if polarity > 0.2:
        return "happy 😊"
    elif polarity < -0.2:
        return "sad 😢"
    else:
        return "neutral 😐"

# Only runs if you manually execute mood_utils.py, not when imported
if __name__ == "__main__":
    entry = input("Write your journal entry: ")
    mood = detect_mood(entry)

    print("Detected mood:", mood)

    if mood == "happy 😊":
        print("Keep smiling! 😄")
    elif mood == "sad 😢":
        print("It's okay to feel down. Try doing something you enjoy. 💖")
    else:
        print("Hope your day picks up! 🌤️")
