import sys
import requests
try:
    if len(sys.argv) == 2:
        bitcoin_no = float(sys.argv[1])
    elif len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
API_URL = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=API_KEY"
response = requests.get(API_URL)
data = response.json()
price = float(data["data"]["priceUsd"])
# python dictatinary data 
price = bitcoin_no * price

print(f"${price:,.4f}")