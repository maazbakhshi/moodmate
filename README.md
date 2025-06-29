# 🎭 MoodMate+ – Your AI-Powered Mood Companion

**MoodMate+** is a Python-based application that acts as your intelligent lifestyle buddy. It analyzes your mood based on daily journal entries and recommends personalized activities based on your **feelings**, **interests**, and **time of day**. The project starts as a Command-Line Interface (CLI) app and evolves into a full **Streamlit-based GUI**.

> Developed by Maaz Bakhshi in an 8-week summer bootcamp to learn Python, AI basics, and software development lifecycle.

---

## 📌 Features

- ✍️ **Mood Journaling**: Enter how you're feeling each day.
- 🧠 **Sentiment Detection**: Uses AI (TextBlob) to detect emotional tone.
- ⏰ **Context-Aware Suggestions**: Combines your mood + time + interests.
- 👤 **User Profiles**: Saves your name, favorite interests, and preferences.
- 🧾 **Mood Logs**: Saves entries and tracks your emotional trends.
- 📈 **Mood Trend Visualization**: Shows your weekly emotional graph.
- 🖼️ **Streamlit GUI**: Easy-to-use interface built in later weeks.
- 🧩 **Modular Architecture**: Easy to extend or integrate new features (like GPT or voice input).

---

## 🏗️ Project Roadmap (8-Week Learning Journey)

| Week | Focus Area | Key Outcomes |
|------|------------|--------------|
| 1 | Python Basics | Build greeting and mood input CLI |
| 2 | Data Structures | Create and save user profiles |
| 3 | AI & Sentiment | Detect moods using TextBlob (Jupyter) |
| 4 | Smart Suggestions | Time + Mood + Interest logic |
| 5 | Integration | Full CLI app (MoodMate+ v1) |
| 6 | Visualization | Mood logs + matplotlib graphs |
| 7 | Streamlit | Convert CLI to web-based GUI |
| 8 | Final Demos | Pitch and present working app |

---

## ✅ Development Goals Checklist

### 🗓️ Core Milestones

- [x] Week 1: Setup Python environment and build basic CLI greeter
- [ ] Week 2: Create user profile system and save to `profile.json`
- [ ] Week 3: Implement mood detection with TextBlob in Jupyter
- [ ] Week 4: Develop suggestion engine based on mood, time, and interests
- [ ] Week 5: Combine modules into fully working CLI app
- [ ] Week 6: Add logging system and plot mood trends with `matplotlib`
- [ ] Week 7: Convert CLI to basic Streamlit app with user inputs
- [ ] Week 8: Finalize UI, prepare demo, and pitch project

### 🔧 Feature Completion

- [ ] User profile creation (name + interests)
- [ ] Journal entry input and mood detection
- [ ] Context-aware activity recommendations
- [ ] Mood log storage (`log.json`)
- [ ] Mood history viewer
- [ ] Mood trend chart
- [ ] Streamlit UI for mood input and suggestions
- [ ] Streamlit dashboard for mood history

### 🌟 Optional Extensions

- [ ] Integrate GPT for dynamic suggestions
- [ ] Add GIF/image support in Streamlit
- [ ] Add voice input support
- [ ] Support multiple users

## 📂 Folder Structure

```bash
MoodMatePlus/
│
├── profile.py             # Create/load user profile
├── mood.py                # Mood detection logic
├── suggestions.py         # Activity recommendation engine
├── moodmate.py            # CLI main app
├── logger.py              # Save mood entries to log.json
├── log.json               # Mood history log
├── profile.json           # User profile storage
├── suggestions.json       # Static suggestion dataset
├── mood_trend.ipynb       # Jupyter notebook for plotting
├── streamlit_app.py       # Final Streamlit web app
└── README.md              # You're here!

