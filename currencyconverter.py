import requests

def currency_converter(amount, from_currency, to_currency):
    api_key = "ec15356e91b704ec2cc6c0b8 "  # You can get your API key from https://www.exchangerate-api.com/
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        rates = data['rates']
        
        # Mapping currency codes to their full names
        currency_names = {
            "USD": "US Dollar",
            "EUR": "Euro",
            "GBP": "British Pound",
            "JPY": "Japanese Yen",
            "CAD": "Canadian Dollar",
            "INR": "Indian Rupee",
            # Add more currencies here
        }
        
        exchange_rate = rates[to_currency]
        converted_amount = amount * exchange_rate
        return converted_amount, currency_names.get(from_currency, from_currency), currency_names.get(to_currency, to_currency)
    except Exception as e:
        print("Error:", e)
        return None, None, None

def main():
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP, INR): ").upper()
        to_currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP, INR): ").upper()

        converted_amount, from_currency_name, to_currency_name = currency_converter(amount, from_currency, to_currency)
        if converted_amount is not None:
            print(f"{amount} {from_currency_name} is equal to {converted_amount:.2f} {to_currency_name}")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    except KeyboardInterrupt:
        print("\nConversion cancelled by user.")

if __name__ == "__main__":
    main()
