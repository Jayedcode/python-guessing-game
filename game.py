import streamlit as st
import pickle
import os
import random

# --- Page Setup ---
st.set_page_config(page_title="🎯 Guessing Game", page_icon="🎲", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            color: #3E64FF;
        }
        .subtitle {
            text-align: center;
            color: #555;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .guess-box {
            background-color: #F0F2F6;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #888;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title & Subtitle ---
st.markdown('<div class="title">🎯 Number Guessing Game</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Guess a number between <strong>1 and 100</strong>!</div>', unsafe_allow_html=True)

# --- Load or Initialize Game State ---
if "jackpot" not in st.session_state or "counter" not in st.session_state:
    if os.path.exists("game_state.pkl"):
        with open("game_state.pkl", "rb") as f:
            saved_state = pickle.load(f)
            st.session_state.jackpot = saved_state.get("jackpot", random.randint(1, 100))
            st.session_state.counter = saved_state.get("counter", 0)
    else:
        st.session_state.jackpot = random.randint(1, 100)
        st.session_state.counter = 0

# --- Guess Section UI ---
with st.container():
    st.markdown('<div class="guess-box">', unsafe_allow_html=True)

    guess = st.number_input("🔢 Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
    submitted = st.button("🚀 Submit Your Guess")

    if submitted:
        st.session_state.counter += 1

        if guess < st.session_state.jackpot:
            st.warning("📈 Try a higher number!")
        elif guess > st.session_state.jackpot:
            st.warning("📉 Try a lower number!")
        else:
            st.success(f"🎉 Correct! You guessed it in {st.session_state.counter} attempts.")
            st.balloons()
            st.info("Game has been reset. Try your luck again! 🎲")
            st.session_state.jackpot = random.randint(1, 100)
            st.session_state.counter = 0

        # Save state
        with open("game_state.pkl", "wb") as f:
            pickle.dump({
                "jackpot": st.session_state.jackpot,
                "counter": st.session_state.counter
            }, f)

    st.caption(f"🧮 Attempts so far: {st.session_state.counter}")

    st.markdown('</div>', unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("## 📊 Game Info")
    st.markdown("- 🔁 Guess until you're right")
    st.markdown("- 🔐 Number is always between **1 and 100**")
    st.markdown("- ⏱️ No time limit — just fun!")

# --- Footer ---
st.markdown('<div class="footer">Made with ❤️ Jayed Akhtar</div>', unsafe_allow_html=True)
