import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_tweet(sentiment,keywords):
    response = model.generate_content([f"Generate a tweet similar to the following sentiment with the given keywords: {sentiment}.\nKeywords: ${', '.join(keywords)}."])
    print(response.text)
