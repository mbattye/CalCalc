import re
import nltk
import ssl
from openai import OpenAI
import os
import streamlit as st

def download_nltk_data():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # List of required NLTK data
    required_nltk_data = ['punkt', 'stopwords']

    for item in required_nltk_data:
        nltk.download(item, quiet=True)

    # Explicitly set the NLTK data path
    nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

# Call the function to download NLTK data
download_nltk_data()

# Get API key
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key not found. Please set it in Streamlit secrets or as an environment variable.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def calculate_calories(user_input):
    foods = [food.strip().lower() for food in user_input.split('\n') if food.strip()]
    
    total_calories = 0
    
    for food in foods:
        # Make API request to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides calorie information for foods. Always respond with a number followed by the word 'calories'."},
                {"role": "user", "content": f"How many calories are in {food}?"}
            ],
            max_tokens=50
        )
        
        # Extract the calorie information from the response
        response_text = response.choices[0].message.content.strip()
        # st.write(f"Response for '{food}': {response_text}")  # Debug output
        
        # Try to extract a number from the response
        match = re.search(r'\d+', response_text)
        if match:
            calories = float(match.group())
            st.write(f"Estimated calories for '{food}': {calories}")
            total_calories += calories
        else:
            st.warning(f"Could not parse calorie information for '{food}'. Response: {response_text}")
    
    return total_calories