import streamlit as st
import re
import random
import string


st.set_page_config(page_title="🔏Password Strength Meter", layout="wide")
st.title("🔏Password Strength Meter")
 
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))



# Function to check password strength
def check_password_strength(password):
    
    score = 0
    
    message = []

    if len(password) >= 8:
        score += 1
    else:
        message.append("❌Password should be at least 8 characters long")

    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    else:
        message.append("❌Password should contain at least one uppercase and one lowercase letter")

    if re.search(r'\d', password):
        score += 1
    else:
        message.append("❌Password should contain at least one number")


    if re.search(r'[!@#$%^&*]' , password):
        score += 1
    else:
        message.append("❌Password should contain at least one special character")

    if score == 5:
        message.append("✅Password is strong")
    elif score == 4 or score == 3:
        
        message.append("✅Password is medium")
    else:
        message.append("❌Password is weak")
       



    if message:
        for msg in message:
            st.markdown(f"**{msg}**")
        
   


password = st.text_input("Enter Your Password", type="password")

if password and st.button("Check Password Strength"):
    check_password_strength(password)

if st.button("Generate Password"):
            sen = generate_password()
            st.markdown(sen)






