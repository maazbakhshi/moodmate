# greeter.py
# To ask for user's name and return a greeting based on the current time

from datetime import datetime

# Ask for user's name
def get_user_name():
    name = input("What's your name? ").strip()
    while name == "":
        print("Name cannot be empty. Try again.")
        name = input("What's your name? ").strip()
    return name

# Return a greeting based on current time
def get_time_based_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Show the greeting to the user
def greet_user(name, greeting):
    print(f"{greeting}, {name}! 🌞")

# Save greeting to log file
def log_greeting(name, greeting):
    with open("greet_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {greeting}, {name}\n")

# --- Run this file directly ---
if __name__ == "__main__":
    name = get_user_name()
    greeting = get_time_based_greeting()
    greet_user(name, greeting)
    log_greeting(name, greeting)


