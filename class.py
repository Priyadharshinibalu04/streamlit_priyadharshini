
import streamlit as st

# Title and description
st.title("🎈 Welcome to My First Streamlit App!")
st.write("This is a simple app that takes user input and displays it.")

# Input fields
name = st.text_input("Enter your name")
language = st.selectbox("Choose your favorite programming language", 
                        ["Python", "Java", "C++", "JavaScript", "Kotlin", "Swift"])
age = st.slider("Select your age", 10, 100, 25)

# Button
if st.button("Submit"):
    st.success(f"Hello **{name}**, aged {age}, who loves **{language}**! 🎉")
