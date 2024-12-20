"""import os
from groq import Groq
from groq import AuthenticationError

# Replace 'your_api_key_here' with your actual Groq API key
api_key = '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'

def validate_api_key(api_key):
    try:
        client = Groq(api_key=api_key)
        # Attempt to retrieve available models as a test request
        models = client.models.list()
        print("API Key is valid. Available models:")
        print(client.models.list())
        for model in models:
            print(f"- {model['id']}: {model['name']}")
    except AuthenticationError:
        print("Invalid API Key. Please check your API credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    validate_api_key(api_key) """


#import groq
#print(dir(groq)) 


from dotenv import load_dotenv
import os
from groq import Groq
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
# Debugging: Check API key
groq_api_key = os.getenv("GROQ_API_KEY")
print(f"GROQ_API_KEY: {groq_api_key}")

# Initialize LLM
try:
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")
    print("LLM Object Created:", llm)
except Exception as e:
    print("Error Creating LLM:", e)

# Verify available models
try:
    client = Groq(groq_api_key=groq_api_key)
    models = client.models.list()
    print("Available Models:", models)
except Exception as e:
    print("Error Fetching Models:", e) 

"""try:
    client = Groq(api_key=groq_api_key)
    response = client.chat.create(
        messages=[{"role": "user", "content": "Test message"}],
        model="gemma2-9b-it",
    )
    print("Chat Response:", response)
except Exception as e:
    print("Error Testing Chat Endpoint:", e) """