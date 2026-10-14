from openai import OpenAI
from dotenv import load_dotenv
import os

###############################
# Load environment variable
################################

load_dotenv()

###############################
# Read Open API key
################################

api_key = os.getenv("OPEN_AI_SECRET_KEY")


###############################
# Create OpenAI Client
################################

client = OpenAI(api_key=api_key)

###############################
# Function to call GPT model
################################




def ask_gpt(prompt):
    response = client.responses.create(
        model= "gpt-5.6-terra",
        input = prompt,
    )
    return response.output_text

