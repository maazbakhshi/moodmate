# user_profile.py
# To ask for user's name and interests and save to a JSON file

import json
import os

def create_profile():
    name = input("What's your name? ").strip()
    interests_input = input("Tell me 3 things you like (comma-separated): ")
    interests = [item.strip() for item in interests_input.split(",")]

    new_profile = {
        "name": name,
        "interests": interests
    }

    profiles = []

    # ✅ Load existing data, upgrade to list if needed
    if os.path.exists("profile.json"):
        with open("profile.json", "r") as f:
            try:
                data = json.load(f)

                # 🔁 Upgrade old dict format to list
                if isinstance(data, dict):
                    profiles = [data]
                elif isinstance(data, list):
                    profiles = data
                else:
                    profiles = []

            except json.JSONDecodeError:
                profiles = []

    # ✅ Add new profile
    profiles.append(new_profile)

    # ✅ Save back as a list
    with open("profile.json", "w") as f:
        json.dump(profiles, f, indent=4)

    print("✅ New profile added to profile.json!")
    return new_profile

# Load profile from JSON
def load_profile():
    with open("profile.json", "r") as f:
        profile = json.load(f)
    return profile

# Show profile nicely
def display_profile(profile):
    print(f"\nWelcome back, {profile['name']}!")
    print("Your interests are:", ", ".join(profile["interests"]))

# --- Run this file directly ---
if __name__ == "__main__":
    profile = create_profile()
    display_profile(profile)