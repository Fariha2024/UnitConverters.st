import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")

def convert_currency(value, from_currency, to_currency):
    """Convert currency using exchangerate-api."""
    if not CURRENCY_API_KEY:
        raise ValueError("API Key is missing. Please check your .env file.")

    url = f"https://v6.exchangerate-api.com/v6/98149fdde5cb57e7070b1e2d/latest/USD"
    
    response = requests.get(url)
    data = response.json()

    if "conversion_rates" not in data:
        raise ValueError("Invalid API response. Check your API key and request.")

    rate = data["conversion_rates"].get(to_currency)

    if rate is None:
        raise ValueError(f"Conversion rate for {to_currency} not found.")

    return value * rate

# Example usage
amount = 100  # Amount to convert
from_currency = "USD"
to_currency = "EUR"

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
