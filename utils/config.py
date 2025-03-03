import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Key (if using a currency API)
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")
print(f"Loaded API Key: {CURRENCY_API_KEY}")

# Default settings
DEFAULT_CURRENCY_FROM = "USD"
DEFAULT_CURRENCY_TO = "EUR"
