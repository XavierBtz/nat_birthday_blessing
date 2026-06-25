import streamlit as st
import datetime
import streamlit.components.v1 as components

# --- CONFIGURATION ---
st.set_page_config(page_title="For Natasia", page_icon="✨", layout="centered")

# --- BULLETPROOF CENTERING & PREMIUM GLASS CSS ---
st.markdown("""
    <style>
    /* Prevent background repeating and force high-end dark gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #1b163a 50%, #101026 100%) !important;
        background-attachment: fixed;
    }
    
    /* Clean custom Title styling */
    .main-title {
        color: #FFD1DC !important; /* Rose Gold */
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        letter-spacing: 3px;
        text-align: center;
        font-size: 2.5rem;
        margin-top: 30px;
        margin-bottom: 5px;
    }
    
    .subtitle {
        color: #B0A8B9;
        text-align: center;
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* Force the button to be completely centered on the screen */
    div.stButton > button {
        background: transparent !important;
        color: #FFD1DC !important;
        border: 1px solid #FFD1DC !important;
        border-radius: 30px !important;
        padding: 12px 45px !important;
        font-family: 'Helvetica Neue', sans-serif !important;
        font-size: 15px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        transition: all 0.4s ease !important;
        display: block !important;
        margin: 25px auto !important;
        box-sizing: border-box;
        box-shadow: 0 4px 15px rgba(255, 209, 220, 0.1) !important;
    }
    
    div.stButton > button:hover {
        background-color: #FFD1DC !important;
        color: #0f0c29 !important;
        box-shadow: 0 0 25px rgba(255, 209, 220, 0.5) !important;
    }
    
    /* Premium Frosted Glass Box */
    .love-note {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px 30px;
        border-radius: 20px;
        color: #FFFFFF;
        font-size: 22px;
        font-family: 'Georgia', serif;
        font-style: italic;
        text-align: center;
        line-height: 1.8;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        margin: 30px auto;
        max-width: 550px;
    }
    
    /* Center container layout for the Spotify player */
    .music-wrapper {
        max-width: 450px;
        margin: 0 auto;
        padding: 0 10px;
    }
    
    /* Center info alert message text */
    .stAlert {
        text-align: center;
        max-width: 450px;
        margin: 20px auto !important;
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

# --- UI LAYOUT ---
st.markdown('<div class="main-title">Natasia Rebecca Nelson</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A daily note, just for you.</div>', unsafe_allow_html=True)

# Clean, structured Spotify Player Box
# (Tip: You can swap out the track ID '4PTG3Z6ehGkBFm3T7Y8Zor' with any song link from Spotify!)
st.markdown('<div class="music-wrapper">', unsafe_allow_html=True)
st.components.v1.html("""
    <iframe style="border-radius:12px;" 
    src="https://open.spotify.com/embed/track/4PTG3Z6ehGkBFm3T7Y8Zor?utm_source=generator&theme=0" 
    width="100%" height="80" frameBorder="0" allowfullscreen="" 
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""", height=80)
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.opened_today_natasia:
    st.markdown(f'<div class="love-note">"{messages[day_index]}"<br><br><span style="font-size: 16px; color: #FFD1DC;">— Nathaniel</span></div>', unsafe_allow_html=True)
    st.info("Your message is locked for the day. Come back tomorrow for a new one. ✨")
else:
    if st.button("Unlock Today's Note"):
        st.session_state.opened_today_natasia = True
        st.rerun()
