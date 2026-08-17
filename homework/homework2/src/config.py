import os
from dotenv import load_dotenv
load_dotenv()
print("Loaded .env (if present)")

def get_key(key, default=None):
    return os.getenv(key, default)

# Set up Project and data directory path
api_key_present = get_key("API_KEY") is not None  
print(f"API_KEY is present: {api_key_present}")
