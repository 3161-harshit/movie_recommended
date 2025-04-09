import streamlit as st
import pandas as pd
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

st.write("Client ID:", client_id)  # Optional: for debugging (remove later)



user_file_path = "users.csv"

page_bg_img = f"""
<style>
.stApp {{
    background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20230703/pngtree-3d-rendered-movie-theatre-with-white-screen-image_3732826.jpg");
    background-attachment: fixed;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# Function to save user data to CSV
def save_user(gmail, name):
    if os.path.exists(user_file_path) and os.path.getsize(user_file_path) > 0:
        users = pd.read_csv(user_file_path)
    else:
        users = pd.DataFrame(columns=["Gmail", "Name"])

    if gmail not in users["Gmail"].values:
        new_user = pd.DataFrame([[gmail, name]], columns=["Gmail", "Name"])
        users = pd.concat([users, new_user], ignore_index=True)
        users.to_csv(user_file_path, index=False)

# UI for login
st.title("🎬 Movie Suggestion App Login")

with st.form("login_form"):
    gmail = st.text_input("📧 Gmail")
    name = st.text_input("👤 Name (optional)")  # Optional name
    password = st.text_input("🔑 Password", type="password")
    submit = st.form_submit_button("Login")

    if submit:
        if gmail and password:
            # Fallback name if not provided
            if not name:
                name = gmail.split("@")[0]

            save_user(gmail, name)
            st.success(f"Welcome, {name}! Redirecting to movie page...")

            # Store in session state and redirect
            st.session_state.logged_in = True
            st.session_state.user = name
            st.switch_page("pages/movies.py")
        else:
            st.warning("Please enter both Gmail and Password.")
