## This script demonstrates how to call the Gemini API using the Google GenAI client library.
# Make sure to install the Google GenAI client library first:
# pip install google-genai

from google import genai

def get_api_key():
    # This function should return your actual API key.
    # For security reasons, do not hardcode your API key in the script.
    # Instead, consider using environment variables or a secure vault, or put it in secure file
    # Open the file in read mode
    with open('gemini_api_key.txt', 'r') as file:
         contents = file.read()
    return contents  # Replace with your actual API key

my_api_key= get_api_key() # Replace with your actual API key

client = genai.Client(api_key=my_api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a simple way."
)
print(response.text)
