import sys
import requests

def main():
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    # Get the number of Bitcoins from the command-line argument
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: The number of Bitcoins must be a valid number.")

    # Fetch the current price of Bitcoin
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Could not fetch Bitcoin price.")

    # Calculate the total cost
    total_cost = bitcoins * price_per_bitcoin

    # Output the cost with four decimal places and commas as thousands separators
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
