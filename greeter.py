from datetime import datetime

def get_user_name():
    return input("What's your name? ")

def get_time_based_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def greet_user(name, greeting):
    print(f"{greeting}, {name}! 🌞")

name = get_user_name()
greeting = get_time_based_greeting()
greet_user(name, greeting)


def log_greeting(name, greeting):
    with open("greet_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {greeting}, {name}\n")

log_greeting(name, greeting)

def get_user_name():
    name = input("What's your name? ").strip()
    while name == "":
        print("Name cannot be empty. Try again.")
        name = input("What's your name? ").strip()
    return name
