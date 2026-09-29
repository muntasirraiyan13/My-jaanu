import streamlit as st
from datetime import datetime
import random
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="For My Jaanu 💕", page_icon="🧸", layout="centered")

# --- CUSTOM CSS FOR 'POOKIE' AESTHETIC ---
st.markdown("""
    <style>
    /* Soft pastel pink background */
    .stApp {
        background-color: #ffe6ea;
    }
    
    /* Glowing romantic header */
    .glow-text {
        font-size: 40px;
        color: #d6336c;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: bold;
        text-shadow: 0 0 10px #ffb3c6, 0 0 20px #ffb3c6;
        margin-bottom: 30px;
    }
    
    /* General text styling */
    h1, h2, h3, p {
        color: #b02a5c !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    /* Cute rounded buttons */
    div.stButton > button {
        background-color: #ffb3c6 !important;
        color: #b02a5c !important;
        border-radius: 25px !important;
        border: 2px solid #ff8fab !important;
        font-weight: bold !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease 0s !important;
    }
    div.stButton > button:hover {
        background-color: #ff8fab !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 143, 171, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'kisses' not in st.session_state:
    st.session_state.kisses = 0
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0

# --- HEADER ---
st.markdown('<div class="glow-text">A Little Digital Love Letter for My Favorite Human 💕✨</div>', unsafe_allow_html=True)
st.divider()

# --- RELATIONSHIP COUNTER ---
st.subheader("⏳ How long I've been the luckiest person:")
# ⬇️ REPLACE THIS DATE WITH YOUR ACTUAL ANNIVERSARY (Year, Month, Day) ⬇️
START_DATE = datetime(2025, 4, 14) 
today = datetime.now()
time_together = today - START_DATE

days = time_together.days
hours = time_together.seconds // 3600

st.write(f"**{days} days and {hours} hours** of loving you... and a million more to go! 🥺❤️")
st.divider()

# --- REASONS WHY I LOVE YOU GENERATOR ---
st.subheader("💌 101 Reasons Why You're My Jaanu")
reasons = [
    "You have the cutest smile in the entire universe.",
    "The way your nose scrunches when you laugh.",
    "You always know exactly how to make my day better.",
    "Your hugs feel like absolute home to me.",
    "You're the only person I'd share my favorite snacks with.",
    "Even when you're being annoying, you're adorably annoying.",
    "You listen to my silly rants and still think I'm cool.",
    "Your eyes hold the stars.",
    "You inspire me to be a better person every single day.",
    "Because you're YOU, and there's no one else I'd rather annoy for the rest of my life.",
    "You make even doing nothing feel like an adventure.",
    "Your voice is my favorite sound."
]

if st.button("Click for a reason! 🌸"):
    random_reason = random.choice(reasons)
    st.success(f"💖 {random_reason}")
    st.balloons()

st.divider()

# --- VIRTUAL HUGS & KISSES COUNTER ---
st.subheader("🧸 Virtual Hugs & Kisses Station")
st.write(f"You have collected **{st.session_state.kisses}** virtual kisses so far! 😘")

if st.button("Send a virtual kiss! 💋"):
    st.session_state.kisses += 1
    st.rerun()

st.divider()

# --- MEMORY LANE / PHOTO GALLERY ---
st.subheader("📸 My personal gallery")
st.write("I used to see these two pictures when I feel sad...")

# SAFE IMAGE LOADER: Prevents the app from crashing if your photos aren't in the folder yet
def show_photo_safely(file_name, fallback_text, caption):
    if os.path.exists(file_name):
        st.image(file_name, caption=caption)
    else:
        st.image(f"https://placehold.co/400x400/ffb3c6/b02a5c?text={fallback_text}", caption=caption)

# Changed from 3 columns to 2 columns for your two specific photos
col1, col2 = st.columns(2)

with col1:
    show_photo_safely("Nuzhat1.jpg", "Nuzhat+1", "I love the picture jaanu 🥰")
with col2:
    show_photo_safely("Nuzhat2.jpg", "Nuzhat+2", "First time seeing you in facebook ❤️")

st.divider()

# --- THE ULTIMATE QUESTION ---
st.subheader("🎀 The Ultimate Question")
st.write("Will you be my forever pookie?")

q_col1, q_col2 = st.columns(2)

with q_col1:
    if st.button("YES! Of course! 🥰"):
        st.balloons()
        st.success("YAYYYYY! 🎉 Best decision ever! I love you so so much! ❤️")
        
        # --- YOUR PERSONAL LOVE LETTER ---
        st.markdown("""
        ### My Secret Love Letter to You 💌
        *Dear Jaanu,*
        
        *Jaanu tomake ami onkkk onkkk onkkk onkkk onkkk valobashi. Shara jibon tomar sathe tomar hoye thakte chai. Tomake valobeshe jete chai. I love you sooooo much jaanu. Amake kokhono chere jayoo na jaanu.*
        
        *Forever Yours,*
        *Raiyuuu* 💕
        """)

with q_col2:
    if st.button("No 🤨"):
        st.session_state.no_clicks += 1
        
        if st.session_state.no_clicks == 1:
            st.error("Error 404: 'No' is not a valid option! Did your hand slip? 🥺")
        elif st.session_state.no_clicks == 2:
            st.error("Wait, seriously? You clicked it AGAIN?! My heart is breaking 💔")
        elif st.session_state.no_clicks == 3:
            st.error("Okay, now you're just being mean! The 'Yes' button is right there! 👉")
        else:
            st.error("I'm locking the 'No' button. You're legally obligated to be my pookie now. 🔒😌")