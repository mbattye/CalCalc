import streamlit as st
from calorie_calculator import calculate_calories

st.title("Daily Calorie Calculator")

user_input = st.text_area("Enter the foods you ate today (one per line):")

if st.button("Calculate Calories"):
    if user_input:
        st.write("Calculating calories...")
        try:
            total_calories = calculate_calories(user_input)
            st.success(f"Total calories consumed: {total_calories:.2f}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some foods before calculating.")
