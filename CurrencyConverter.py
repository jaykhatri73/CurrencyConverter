# currency database
exchange_rates = {
    'USD': {'EUR': 0.92, 'GBP': 0.79, 'CAD': 1.32, 'INR': 81.85},
    'EUR': {'USD': 1.09, 'GBP': 0.86, 'CAD': 1.45, 'INR': 89.32},
    'GBP': {'USD': 1.27, 'EUR': 1.16, 'CAD': 1.68, 'INR': 103.93},
    'CAD': {'USD': 0.76, 'EUR': 0.69, 'GBP': 0.59, 'INR': 61.79},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0096, 'CAD': 0.016}
}

# declaring available currency in the database
print("Available currencies to convert are: USD | EUR | GBP | CAD | INR")
print("Conversion rates were last updated on 02 July, 2023")

# handling wrong inputs from user


def convert_currency(x, y, z):
    if y == z:
        return x

    if y not in exchange_rates or z not in exchange_rates:
        return None

# conversion calculator
    rate = exchange_rates[from_currency][to_currency]
    conversion = amount * rate
    return conversion


# taking input from user
amount = float(input("Enter the amount to convert: "))
from_currency = input("Convert Currency FROM: ").upper()
to_currency = input("Convert Currency TO: ").upper()

# calling function
converted_amount = convert_currency(amount, from_currency, to_currency)

# desplaying results to user
if converted_amount is None:
    print("Invalid currency codes or exchange rate not available.")
else:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
