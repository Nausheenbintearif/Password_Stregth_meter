
import streamlit as st
import re
import random

# Special characters for validation and generation
special_chars = "!@#$%^&*"
blacklist = ['password', '123456', '12345678', 'qwerty', 'abc123', 'password123', 'admin', 'letmein']

def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in blacklist:
        return 1, ["This password is too common and easily guessable. Avoid using common passwords."]

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make it at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Use both UPPERCASE and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one digit (0–9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    if len(password) >= 12:
        score += 1

    return score, suggestions

def generate_strong_password(length=12):
    if length < 8:
        length = 8
    base = (
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") +
        random.choice("abcdefghijklmnopqrstuvwxyz") +
        random.choice("0123456789") +
        random.choice(special_chars)
    )
    rest = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" + special_chars, k=length - 4))
    password = list(base + rest)
    random.shuffle(password)
    return ''.join(password)

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")

menu = st.sidebar.selectbox("Choose an option", ["Check Password", "Generate Strong Password"])

if menu == "Check Password":
    st.subheader("🧪 Check Password Strength")
    password = st.text_input("Enter your password", type="password")

    if password:
        score, suggestions = check_password_strength(password)

        if score >= 5:
            st.success("✅ Password Strength: STRONG")
        elif score >= 3:
            st.warning("⚠️ Password Strength: MODERATE")
            
