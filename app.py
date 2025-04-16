import streamlit as st
import random

def get_motivational_quote():
    quotes = [
        "💡 *Failure is not the opposite of success; it's part of success!*",
        "🧠 *Your only limit is your mind. Keep learning, keep growing!*",
        "🚀 *Dream big, work hard, stay focused, and surround yourself with good people.*",
        "🔁 *A growth mindset turns obstacles into opportunities.*",
        "🌱 *Every expert was once a beginner. Keep pushing forward!*"
    ]
    return random.choice(quotes)

# App Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟 Growth Mindset Web App 🌟</h1>", unsafe_allow_html=True)

# Introduction
st.markdown("### Welcome to the Growth Mindset Hub! 👋")
st.write("This interactive app is here to boost your mindset, help you stay motivated, and support your personal development journey!")

# Divider
st.markdown("---")

# User Input Section
st.markdown("#### 🛠️ What's your personal goal?")
user_goal = st.text_input("Tell us one thing you want to improve:", placeholder="e.g., Time management, communication, confidence")

if user_goal:
    st.success(f"🔥 Awesome! Keep improving your **{user_goal}**. Remember, growth takes time and consistency.")
    st.info("💡 Tip: Break your goal into small steps and celebrate each win!")

# Divider
st.markdown("---")

# Motivation Section
st.markdown("#### ✨ Your Daily Dose of Inspiration")

if st.button("💬 Get Inspired!"):
    st.success(get_motivational_quote())

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Keep growing. Keep going. 🌱</p>", unsafe_allow_html=True)
