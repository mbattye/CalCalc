import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from openai import OpenAI
import os
import streamlit as st

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

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
        response_text = response.choices[0].message.content.strip()
        
        # Use regex to find the first number in the response
        match = re.search(r'\d+', response_text)
        if match:
            calories = float(match.group())
        else:
            print(f"Could not parse calorie information for {food_query}")
            print(f"AI response: {response_text}")
            calories = 0
        
        total_calories += calories
        print(f"Estimated calories for '{food}': {calories}")
    
    return total_calories