import streamlit as st
from calorie_calculator import calculate_calories

st.title("Daily Calorie Calculator")

user_input = st.text_area("Enter the foods you ate today (one per line):")

if st.button("Calculate Calories"):
    if user_input:
        total_calories = calculate_calories(user_input)
        st.success(f"Total calories consumed: {total_calories:.2f}")
    else:
        st.warning("Please enter some foods before calculating.")

st.markdown("---")
st.markdown("### How to use:")
st.markdown("1. Enter the foods you ate today, one per line.")
st.markdown("2. Click 'Calculate Calories' to see your total calorie intake.")
st.markdown("3. The app will process your input and display the result.")

# Add this at the end of the file
if __name__ == "__main__":
    import os
    if not os.path.exists('streamlit_static'):
        os.makedirs('streamlit_static')
    with open('streamlit_static/index.html', 'w') as f:
        f.write('<html><body><script>window.location.href = "/calcalc";</script></body></html>')
