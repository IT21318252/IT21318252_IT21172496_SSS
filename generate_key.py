import pickle
from pathlib import Path

import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

# User data
names = ["Ammar Parker", "Shuhaib Miller"]
usernames = ["aparker", "smiller"]
passwords = ["abc123", "def456"]

# Hash passwords
hashed_passwords = Hasher(passwords).generate()

# Save hashed passwords to a file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

print("Hashed passwords saved successfully.")
