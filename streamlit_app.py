import streamlit as st
from calorie_calculator import calculate_calories, download_nltk_data

# Ensure NLTK data is downloaded
download_nltk_data()

st.title("Daily Calorie Calculator")

user_input = st.text_area("Enter the foods you ate today (one per line):")

if st.button("Calculate Calories"):
    if user_input:
        total_calories = calculate_calories(user_input)
        st.success(f"Total calories consumed: {total_calories:.2f}")
    else:
        st.warning("Please enter some foods before calculating.")
