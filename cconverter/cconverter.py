import requests


def currency_converter():
    # Input the base currency
    base_currency = input().strip().lower()
    url = f"http://www.floatrates.com/daily/{base_currency}.json"

    # Initialize the cache
    cache = {}

    try:
        # Fetch exchange rates data
        response = requests.get(url)
        response.raise_for_status()
        rates = response.json()

        # Preload USD and EUR into the cache
        if 'usd' in rates:
            cache['usd'] = rates['usd']['rate']
        if 'eur' in rates:
            cache['eur'] = rates['eur']['rate']
    except requests.RequestException:
        print("Failed to fetch exchange rates. Please check your internet connection.")
        return

    # Process user input for exchanges
    while True:
        target_currency = input().strip().lower()
        if not target_currency:  # Exit condition
            break

        amount = input().strip()
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        print("Checking the cache...")
        if target_currency in cache:
            print("Oh! It is in the cache!")
            rate = cache[target_currency]
        else:
            print("Sorry, but it is not in the cache!")
            if target_currency in rates:
                rate = rates[target_currency]['rate']
                cache[target_currency] = rate
            else:
                print(f"No exchange rate available for {target_currency}.")
                continue

        # Calculate and display the result
        exchanged_amount = round(amount * rate, 2)
        print(f"You received {exchanged_amount} {target_currency.upper()}.")


# Run the converter
currency_converter()