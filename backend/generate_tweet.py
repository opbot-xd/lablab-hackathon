import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_tweet(sentiment,keywords,query):
    print(keywords)
    response = model.generate_content([f"Generate a tweet similar to the following sentiment on {query} with the given keywords with the corresponding preferance of the keyword beside it: {sentiment}.\nKeywords: ${keywords}. \nIf some keywords are too offensive,stereotypical or harmful, please ignore them. When we say negative sentiment, we only want to generate a dissenting tweet. We do not promote offensive and harmful content."])
    return response.text