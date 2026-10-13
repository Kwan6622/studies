# 20/07/2026
# Implement a Bitcoin price calculator.
# Accept the number of Bitcoins the user wants to buy as a command-line argument.
# Query the CoinCap API to get the current Bitcoin price in USD.
# Calculate and display the total cost of the requested Bitcoin amount.
# Format the output with a thousands separator and 4 decimal places.
# Handle invalid command-line arguments and API request errors.

# Steps:
# 1. Import sys and requests.
# 2. Check that the user provides exactly one command-line argument.
# 3. Convert the argument into a float.
#    - If conversion fails, exit with an error message.
# 4. Send a request to the CoinCap Bitcoin API.
# 5. Handle any request exceptions.
# 6. Extract the current Bitcoin price from the JSON response.
# 7. Calculate:
#       total cost = bitcoin amount * current bitcoin price
# 8. Print the result:
#       - Prefix with "$"
#       - Use comma as a thousands separator.
#       - Display exactly 4 decimal places.

import requests
import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Missing Command-line Argument!")

        elif len(sys.argv) > 2:
            sys.exit("Too Many Command-line Argument!")

        else:
            amount = float(sys.argv[1])

            r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0b8937c5d66eaecddb03176d9629d49ca9b457b48e262ee86f78521771fa4e10")
            bitcoin = r.json()

            print(f'${float(bitcoin["data"]["priceUsd"]) * amount:,.4f}')

    except requests.RequestException:
        sys.exit("Could not connect to API server!")

    except ValueError:
        sys.exit("Command-line Argument is not a number!")

if __name__ == "__main__":
    main()