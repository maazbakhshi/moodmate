# streamlit_app.py

import streamlit as st
import json
from datetime import datetime
from textblob import TextBlob
from utils.mood_utils import detect_mood
from utils.suggestions_utils import get_time_of_day, suggest_activity
from utils.profile_utils import load_profile, display_profile, create_profile
from moodmate import save_journal_entry
import matplotlib.pyplot as plt
import os

# Plot mood trend
def plot_mood_trend(logs):
    mood_map = {"happy": 1, "neutral": 0, "sad": -1}
    dates = []
    mood_scores = []

    for entry in logs:
        date = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M")
        mood_label = entry["mood"].split()[0]
        score = mood_map.get(mood_label, 0)
        dates.append(date)
        mood_scores.append(score)

    plt.figure(figsize=(10, 4))
    plt.plot(dates, mood_scores, marker="o")
    plt.title("Mood Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Mood Score")
    plt.grid(True)
    st.pyplot(plt)

# Display all entries
def show_past_entries(logs):
    st.subheader("📖 Past Journal Entries")
    for entry in logs[::-1]:
        st.markdown(f"**{entry['timestamp']}** - *{entry['mood']}*")
        st.markdown(f"> {entry['entry']}")
        st.markdown("---")


# --- Streamlit UI ---

st.set_page_config(page_title="MoodMate+", page_icon="🎭")
st.title("🎭 MoodMate+")

profile = load_profile()
if not profile:
    st.error("No profile found. Please run user_profile.py first to create one.")
    st.stop()

# Sidebar navigation
section = st.sidebar.radio("Choose a section", ["📓 Journal", "💡 Get Suggestion", "📈 Mood Graph", "📘 Past Entries", "👤 View Profile"])

# Journal Entry
if section == "📓 Journal":
    st.subheader("📝 How are you feeling today?")
    journal_entry = st.text_area("Write your journal entry:")

    if st.button("Analyze Mood"):
        if journal_entry.strip() == "":
            st.warning("Please write something first!")
        else:
            mood = detect_mood(journal_entry)
            st.success(f"Detected mood: **{mood}**")
            save_journal_entry(journal_entry, mood)

# Suggestion
elif section == "💡 Get Suggestion":
    st.subheader("💡 Personalized Suggestion")
    entry = st.text_input("How are you feeling today?")
    if st.button("Get Suggestion"):
        if entry.strip() == "":
            st.warning("Enter something first!")
        else:
            mood = detect_mood(entry)
            time = get_time_of_day()
            interests = profile["interests"]
            suggestion = suggest_activity(mood, interests, time)
            st.write("Detected mood:", mood)
            st.write("Time of day:", time)
            st.success(f"👉 {suggestion}")

# Mood Trend
elif section == "📈 Mood Graph":
    st.subheader("📊 Mood Trend")
    if os.path.exists("log.json"):
        with open("log.json", "r") as f:
            logs = json.load(f)
        if logs:
            plot_mood_trend(logs)
        else:
            st.info("No entries found to plot.")
    else:
        st.info("No entries found yet.")

# View Past Entries
elif section == "📘 Past Entries":
    if os.path.exists("log.json"):
        with open("log.json", "r") as f:
            logs = json.load(f)
        if logs:
            show_past_entries(logs)
        else:
            st.info("No journal entries found.")
    else:
        st.info("No entries found yet.")

# Profile
elif section == "👤 View Profile":
    st.subheader("👤 Your Profile")
    st.write("**Name:**", profile["name"])
    st.write("**Interests:**", ", ".join(profile["interests"]))
