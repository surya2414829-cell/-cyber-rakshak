import streamlit as st
import re

# Page Config
st.set_page_config(page_title="Cyber Rakshak", page_icon="🛡️", layout="centered")

st.title("🛡️ Cyber Rakshak")
st.subheader("Meeru Safe ga Unnara? Check chesukondi!")

st.markdown("---")

# 1. PHISHING LINK CHECKER
st.header("1. Link Safe ye na? 🔗")
url = st.text_input("Anumaanam unna Link ikkada paste chey:")
if st.button("Link ni Check Chey"):
    if url:
        suspicious_words = ['free-money', 'lottery', 'bank-login', 'verify-now', 'urgent']
        if any(word in url.lower() for word in suspicious_words) or url.count('-') > 3 or "http://" in url:
            st.error("⚠️ DANGER! Idi Phishing Link ayi undavachu! Click cheyaku!")
        else:
            st.success("✅ Link safe la anipistondi. Aina careful ga undandi.")
    else:
        st.warning("Link enter cheyandi.")

st.markdown("---")

# 2. PASSWORD STRENGTH CHECKER
st.header("2. Password Strong ga Unda? 🔑")
password = st.text_input("Nee Password ni test chesuko:", type="password")
if password:
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1
    
    if score <= 2:
        st.error(f"Weak Password - Score {score}/4")
    elif score == 3:
        st.warning(f"Medium Password - Score {score}/4")
    else:
        st.success(f"Strong Password! - Score {score}/4")

st.markdown("---")

# 3. CYBER TIPS
st.header("3. Cyber Safety Tips 💡")
st.info("""
- Bank OTP evariki cheppakandi
- Free Recharge links click cheyoddu
- Unknown APK files install cheyoddu
- Prathi app ki same password vadakandi
""")

st.markdown("Made with ❤️ by Surya")
