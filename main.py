import streamlit as st
import datetime
import streamlit.components.v1 as components

# --- CONFIGURATION ---
st.set_page_config(page_title="For Natasia", page_icon="✨")

# --- PREMIUM "GLASSMORPHISM" CSS ---
st.markdown("""
    <style>
    /* Sleek, deep romantic background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Elegant Title */
    h1 {
        color: #FFD1DC !important; /* Rose Gold */
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        letter-spacing: 2px;
        text-align: center;
        padding-top: 20px;
    }
    
    .subtitle {
        color: #E0E0E0;
        text-align: center;
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 16px;
        margin-bottom: 40px;
    }

    /* Centered, glowing button */
    div.stButton { text-align: center; }
    
    .stButton>button {
        background: transparent;
        color: #FFD1DC;
        border: 1px solid #FFD1DC;
        border-radius: 30px;
        padding: 12px 35px;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 16px;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: all 0.4s ease;
        margin: 20px auto;
    }
    
    .stButton>button:hover {
        background-color: #FFD1DC;
        color: #0f0c29;
        box-shadow: 0 0 20px rgba(255, 209, 220, 0.4);
    }
    
    /* Frosted Glass Message Box */
    .love-note {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px 30px;
        border-radius: 20px;
        color: #FFFFFF;
        font-size: 22px;
        font-family: 'Georgia', serif;
        font-style: italic;
        text-align: center;
        line-height: 1.8;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- DAILY MESSAGES ---
messages = [
    "I love you more than words can say. You are my favorite part of every day.",
    "Just a daily reminder that you are the most beautiful person I know, inside and out.",
    "Whenever I think about my future, you are always the brightest part of it.",
    "Thank you for being exactly who you are. I wouldn't change a single thing.",
    "Even on the most ordinary days, you make my life feel extraordinary.",
    "I am so incredibly lucky to call you mine. Have a wonderful day, gorgeous.",
    "You are my safe space, my biggest inspiration, and my greatest love."
]

# --- LOGIC ---
today = datetime.date.today()
day_index = today.timetuple().tm_yday % len(messages)

if 'opened_today_natasia' not in st.session_state:
    st.session_state.opened_today_natasia = False
    st.session_state.last_date_natasia = None

if st.session_state.last_date_natasia != today:
    st.session_state.opened_today_natasia = False
    st.session_state.last_date_natasia = today

# --- UI ---
st.title("Natasia Rebecca Nelson")
st.markdown('<div class="subtitle">A daily note, just for you.</div>',
            unsafe_allow_html=True)

# Optional: Embed her favorite song or a playlist (Replace the src link with any Spotify embed link)
st.components.v1.html("""
    <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/68dGKf5eIchw0bxpuhk4g8?utm_source=generator&si=0a413f06accf4df6" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""", height=100)

if st.session_state.opened_today_natasia:
    # The Reveal
    st.markdown(
        f'<div class="love-note">"{messages[day_index]}"<br><br><span style="font-size: 16px; color: #FFD1DC;">— Nathaniel</span></div>', unsafe_allow_html=True)
    st.write("")
    st.info("Your message is locked for the day. Come back tomorrow for a new one. ✨")
else:
    if st.button("Unlock Today's Note"):
        st.session_state.opened_today_natasia = True
        st.rerun()
