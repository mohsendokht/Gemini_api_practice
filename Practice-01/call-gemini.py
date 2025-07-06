## This script demonstrates how to call the Gemini API using the Google GenAI client library.
# Make sure to install the Google GenAI client library first:
# pip install google-genai

#import google.generativeai as genai



# model = genai.GenerativeModel("gemini-1.5-pro")
# response = model.generate_content(
#     "What is the capital of France?",
#     generation_config={
#         "temperature": 0.5,
#         "max_output_tokens": 50
#     }
# )

from google import genai

my_api_key="your actual API key"  # Replace with your actual API key
print(my_api_key)
print("Calling Gemini API... my api kye is: ", my_api_key)
client = genai.Client(api_key=my_api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)
