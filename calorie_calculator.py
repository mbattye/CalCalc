import re
import nltk
import ssl
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
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
        try:
            nltk.data.find(f'tokenizers/{item}')
        except LookupError:
            nltk.download(item)

# Call the function to download NLTK data
download_nltk_data()

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def calculate_calories(user_input):
    # Tokenize and clean the input
    foods = [food.strip().lower() for food in user_input.split('\n') if food.strip()]
    
    total_calories = 0
    
    for food in foods:
        # Process each food item
        tokens = word_tokenize(food)
        tokens = [token for token in tokens if token not in stopwords.words('english')]
        
        # Join tokens back into a string for API request
        food_query = ' '.join(tokens)
        
        # Make API request to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides calorie information for foods."},
                {"role": "user", "content": f"How many calories are in {food_query}? Please respond with just the number of calories."}
            ],
            max_tokens=50
        )
        
        # Extract the calorie information from the response
        try:
            calories = float(response.choices[0].message.content.strip())
        except ValueError:
            print(f"Could not parse calorie information for {food_query}")
            calories = 0
        
        total_calories += calories
    
    return total_calories