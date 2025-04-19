# import streamlit as st
# from cryptography.fernet import Fernet # type: ignore
# from cryptography.hazmat.backends import default_backend # type: ignore
# from cryptography.hazmat.primitives import hashes # type: ignore
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # type: ignore
# import os
# import base64
# import json
# import time


# st.set_page_config(page_title="🔏 Secure File Storage", page_icon="🔒", layout="wide")

# DATA_FILE = "data.json"
# USERS_FILE = "users.json"


# failed_attempts = 0
# last_failed_attempt_time = 0
# LOCKOUT_DURATION = 30

# KEY = Fernet.generate_key()
# cipher = Fernet(KEY)

# def load_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as f:
#             return json.load(f)
#     return {}

# def load_user_data():
#     if os.path.exists(USERS_FILE):
#         with open(USERS_FILE, "r") as f:
#             return json.load(f)
#     return {}

# def save_data(data):
#     with open(DATA_FILE, "w") as f:
#         json.dump(data, f)


# def save_user_data(users):
#     with open(USERS_FILE,"w") as f:
#         json.dump(users , f)

# def generate_hash_passkey(passkey: str , salt: bytes) -> bytes:
#     kdf =PBKDF2HMAC(
#         algorithm = hashes.SHA256(),
#         length =  32,
#         salt = salt,
#         iterations = 100000,
#         backend = default_backend()

#     )
#     key = base64.urlsafe_b64decode(kdf.derive(passkey.encode()))
#     return Fernet(key)
    

# def encrypt_data(text,passkey,salt):
#     fernet = generate_hash_passkey(passkey,salt)
#     return fernet.encrypt(text.encode()).decode()


# users = load_user_data()
# stored_data = load_data()
# def decrypt_data(encrypted_data , passkey , user):
#     global failed_attempts , last_failed_attempt_time
#     if time.time() - last_failed_attempt_time > LOCKOUT_DURATION:
#         failed_attempts = 0
    
#     salt = base64.b64decode(users[user]["salt"])
#     hashed_passkey = generate_hash_passkey(passkey , salt)

#     if user in stored_data and encrypted_data in stored_data:
#         if stored_data[user][encrypted_data]["passkey"] == hashed_passkey:
#             failed_attempts = 0
#             fernet = generate_hash_passkey(passkey , salt)
#             return fernet.decrypt(encrypt_data.encode()).decode()
        
        

#         failed_attempts += 1
#         last_failed_attempt_time = time.time()
#         return None
    

# st.title("🔏 Secure Data Encyption System")



# menu = ["Home" , "Register" , "Login" , "Store Data" , "Retrieve Data"]

# choice = st.selectbox("Navigation" , menu)
# if choice == "Home":
#     st.subheader("🏠Welcome to the Secure Data Encyption System!!")
#     st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

# elif choice == "Register":
#     st.subheader("📄 Register Now!!")
#     username = st.text_input("Username:")
#     password = st.text_input("Password:" , type="password")
#     confirm_password = st.text_input("Confirm Password:" , type="password")

#     if st.button("Register"):
#         if username and password and password == confirm_password:
#             salt = os.urandom(16)
#             hashed_password = generate_hash_passkey(password , salt)
#             users[username] = {"password":hashed_password , "salt":base64.b64encode(salt).decode()}
#             save_user_data(users)
#             st.success("✅ Registration Successfull! You can now login!")

#         else:
#             st.error("⚠ Please ensure password matches and all fields are filled.")


# elif choice == "Login":
#     st.subheader("🔑 User Login!")
#     username = st.text_input("Username:")
#     password = st.text_input("Password:" , type="password")

#     if st.button("Login"):
#         if username in users:
#             salt = base64.b64decode(users[username]["salt"])
#             hashed_password = generate_hash_passkey(password , salt)
#             if users[username]["password"] == hashed_password:
#                 st.session_state.logged_in_user = username
#                 st.success(f"✅ Welcome! {username}")
#                 st.experimental_rerun()
#             else:
#                 st.error("❌ Incorrect username or password")
#         else:

#             st.error("❌ User not found!")

# elif choice == "Store Data" and "logged_in_user" in st.session_state:
#     st.subheader("📂 Store Data Securely!")
#     user_data = st.text_area("Enter Data")
#     passkey = st.text_input("Enter passkey:",type="password")


#     if st.button("Encrypt & Save"):
#         if user_data and passkey:
#             username = st.session_state.logged_in_user
#             salt = base64.b64decode(users[username]["salt"])

#             hashed_passkey = generate_hash_passkey(passkey , salt)

#             encrypted_text = encrypt_data(user_data , passkey , salt)
            
#             if username not in stored_data:
#                 stored_data[username] = {}

#                 stored_data[username][encrypted_text] = {"encrypted_text":encrypted_text , "passkey":hashed_passkey}
#             save_data(stored_data)
#             st.success("✅ Data Stored Successfully!")
#         else:
#             st.error("⚠ Both fields are required")


# elif choice == "Retrieve Data" and "logged_in_user" in st.session_state:
#     st.subheader("🔎 Retrieve Data")
#     encrypted_text = st.text_input("Enter Encrypted Data:")
#     passkey = st.text_input("Enter Passkey:", type="password")

#     if st.button("Decrypt"):
#         if encrypted_text and passkey:
#             username = st.session_state.logged_in_user
#             decrypt_text = decrypt_data(encrypted_text , passkey , username)
#             if decrypt_text:
#                 st.success(f"✅ Decrypted Data {decrypt_text}")
#             else:
#                 failed_attempts += 1
#                 remaining = 3 - failed_attempts
#                 st.error(f"⚠ Incorrect passkey! Attempts remaining {remaining}")
#             if failed_attempts >= 3:
#                 st.warning("⚠ Too many attempts. Redirecting to login page")
#                 st.experimental_rerun()
#         else:
#             st.error("⚠ Both field are required!")



            



    




import streamlit as st
import hashlib
import json
import time
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os

st.set_page_config(page_title="Secure Data Encryption", page_icon="🛡️")

# ------------------- CSS for UI -------------------
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .title {
        font-size: 36px;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        color: #34495e;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 0.6em 1.2em;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- Utility Functions -------------------
def generate_key(passkey: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passkey.encode()))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------- File Management -------------------
DATA_FILE = "data.json"
USERS_FILE = "users.json"
LOCKOUT_DURATION = 60  # seconds

# Load or create data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)
else:
    stored_data = {}

if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

# ------------------- Session State -------------------
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = None

# ------------------- Navigation -------------------
menu = ["Home", "Login", "Store Data", "Retrieve Data", "Logout"]
choice = st.sidebar.selectbox("Navigation", menu)

# ------------------- Pages -------------------
if choice == "Home":
    st.markdown('<div class="title">🔐 Secure Encryption App</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Built with Streamlit | PBKDF2 | Multi-User Login | JSON Storage</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("✅ Encrypt & store sensitive text.")
        st.markdown("🔐 Protected by secure hashing (PBKDF2).")
        st.markdown("👥 Each user has separate data.")
        st.markdown("📁 All data saved securely in `data.json`.")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", width=200)

elif choice == "Login":
    st.markdown('<div class="title">🔑 Login or Register</div>', unsafe_allow_html=True)
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("🔓 Login / Register"):
        if username and password:
            hashed = hash_password(password)
            if username in users:
                if users[username]["password"] == hashed:
                    st.session_state.current_user = username
                    st.success("✅ Logged in successfully!")
                    st.session_state.failed_attempts = 0
                else:
                    st.error("❌ Incorrect password!")
            else:
                salt = os.urandom(16)
                users[username] = {"password": hashed, "salt": base64.b64encode(salt).decode()}
                with open(USERS_FILE, "w") as f:
                    json.dump(users, f)
                st.success("✅ Registered & Logged in!")
                st.session_state.current_user = username

elif choice == "Store Data":
    if not st.session_state.current_user:
        st.warning("🔒 Please login first.")
    else:
        st.markdown('<div class="title">📂 Store Your Secret Data</div>', unsafe_allow_html=True)
        text = st.text_area("📝 Enter your text")
        passkey = st.text_input("🛡️ Create a secure passkey", type="password")

        if st.button("🔐 Encrypt & Save"):
            salt = base64.b64decode(users[st.session_state.current_user]["salt"])
            key = generate_key(passkey, salt)
            f = Fernet(key)
            encrypted_text = f.encrypt(text.encode()).decode()
            stored_data[st.session_state.current_user] = stored_data.get(st.session_state.current_user, [])
            stored_data[st.session_state.current_user].append(encrypted_text)

            with open(DATA_FILE, "w") as f:
                json.dump(stored_data, f)

            st.success("✅ Your data has been encrypted and saved.")

elif choice == "Retrieve Data":
    if not st.session_state.current_user:
        st.warning("🔒 Please login first.")
    else:
        st.markdown('<div class="title">🔍 Retrieve Your Data</div>', unsafe_allow_html=True)

        if st.session_state.lockout_time and time.time() - st.session_state.lockout_time < LOCKOUT_DURATION:
            st.error("⏱️ You are locked out. Please wait before trying again.")
        else:
            entries = stored_data.get(st.session_state.current_user, [])
            if not entries:
                st.info("ℹ️ No data stored yet.")
            else:
                encrypted_text = st.selectbox("🔐 Select Encrypted Entry", entries)
                passkey = st.text_input("🔑 Enter Your Passkey", type="password")

                if st.button("🔓 Decrypt"):
                    salt = base64.b64decode(users[st.session_state.current_user]["salt"])
                    key = generate_key(passkey, salt)
                    f = Fernet(key)
                    try:
                        decrypted = f.decrypt(encrypted_text.encode()).decode()
                        st.success(f"✅ Decrypted Data: {decrypted}")
                        st.session_state.failed_attempts = 0
                    except:
                        st.session_state.failed_attempts += 1
                        attempts_left = 3 - st.session_state.failed_attempts
                        st.error(f"❌ Wrong passkey! Attempts left: {attempts_left}")

                        if st.session_state.failed_attempts >= 3:
                            st.session_state.lockout_time = time.time()
                            st.error("🔒 Too many failed attempts! Please wait before trying again.")

elif choice == "Logout":
    st.session_state.current_user = None
    st.success("🚪 You have been logged out.")