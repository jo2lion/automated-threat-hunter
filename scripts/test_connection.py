import os
import vt
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv('VT_API_KEY')

# Initialize the client
client = vt.Client(api_key)

try:
    # Test connection by looking up google.com
    domain = client.get_object("/domains/google.com")
    print(f"Successfully connected! Domain: {domain.id}")
    print(f"Reputation score: {domain.reputation}")
finally:
    client.close()