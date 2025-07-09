# moodmate.py

import json
from datetime import datetime
from utils.profile_utils import load_profile, display_profile
from utils.mood_utils import detect_mood
from utils.suggestions_utils import get_time_of_day, suggest_activity


# --- Save a journal entry and detected mood ---
def save_journal_entry(entry, mood):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "entry": entry,
        "mood": mood
    }

    try:
        with open("log.json", "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    logs.append(log_entry)

    with open("log.json", "w") as f:
        json.dump(logs, f, indent=4)

    print("✅ Journal entry saved!")


# --- Menu interface ---
def main_menu():
    print("\n📘 Welcome to MoodMate+")
    print("1. Enter mood journal")
    print("2. Get suggestion")
    print("3. View profile")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        entry = input("Write your journal entry: ")
        mood = detect_mood(entry)
        print("Detected mood:", mood)
        save_journal_entry(entry, mood)

    elif choice == "2":
        profile = load_profile()
        interests = profile[-1]["interests"]
        entry = input("How are you feeling today?\n")
        mood = detect_mood(entry)
        time = get_time_of_day()
        suggestion = suggest_activity(mood, interests, time)
        print(f"Your mood: {mood}")
        print(f"Time: {time}")
        print("👉 Suggestion:", suggestion)

    elif choice == "3":
        profile = load_profile()
        print("\n👤 Your Profile:")
        for entry in profile:
            print(f"Interests: {', '.join(entry['interests'])}")

    elif choice == "4":
        print("👋 Goodbye!")
        exit()

    else:
        print("Invalid option. Try again.")

# --- Run the app in a loop ---
if __name__ == "__main__":
    while True:
        main_menu()
