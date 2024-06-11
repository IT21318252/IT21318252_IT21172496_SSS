import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

# --- USER AUTHENTICATION ---
names = ["Ammar Parker", "Shuhaib Miller"]
usernames = ["aparker", "smiller"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# Proper instantiation of Authenticate
authenticator = stauth.Authenticate(
    names=names,
    usernames=usernames,
    hashed_passwords=hashed_passwords,
    name="main",
    key="abcdef",
    cookie_expiry_days=30
)

def login():
    name, authentication_status, username = authenticator.login("Login")
    return name, authentication_status, username
