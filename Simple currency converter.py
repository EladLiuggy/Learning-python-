#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

class CurrencyConverter:  
    def __init__(self, base_currency="USD"):
        self.base_currency = base_currency
        self.api_url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        self.rates = {}  
        self.history = []  

    def fetch_exchange_rates(self):
        """Fetch exchange rates from the API."""
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                data = response.json()
                self.rates = data["rates"]
                print(f"Exchange rates updated successfully for base currency: {self.base_currency}")
            else:
                print("Error: Failed to fetch exchange rates.")
        except Exception as e:
            print(f"An error occurred while fetching exchange rates: {e}")

    def convert_currency(self, amount, target_currency):
        """Convert an amount to the target currency."""
        if target_currency in self.rates:
            converted_amount = amount * self.rates[target_currency]

            self.history.append((amount, self.base_currency, converted_amount, target_currency))
            return converted_amount
        else:
            print(f"Error: Target currency '{target_currency}' not found.")
            return None

    def show_conversion_history(self):
        """Display recent conversions."""
        if self.history:
            print("\nRecent Conversions:")
            for entry in self.history:
                amount, base, converted, target = entry
                print(f"{amount} {base} = {converted:.2f} {target}")
        else:
            print("No conversions available in history.")


def display_menu():
    """Display the application menu."""
    print("\nMenu:")
    print("1. Check Exchange Rate")
    print("2. Convert Currency")
    print("3. View Conversion History")
    print("4. Exit")

def main():
    """Main function to run the program."""
    print("Welcome to the Currency Exchange Rate Checker!")
    base_currency = input("Enter your base currency (e.g., USD): ").upper()
    converter = CurrencyConverter(base_currency)
    
    # Fetch initial exchange rates
    converter.fetch_exchange_rates()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            target_currency = input("Enter target currency (e.g., EUR): ").upper()
            if target_currency in converter.rates:
                print(f"1 {converter.base_currency} = {converter.rates[target_currency]} {target_currency}")
            else:
                print(f"Currency '{target_currency}' not found in exchange rates.")
        
        elif choice == "2":
            try:
                amount = float(input(f"Enter the amount in {converter.base_currency}: "))
                target_currency = input("Enter target currency (e.g., EUR): ").upper()
                converted_amount = converter.convert_currency(amount, target_currency)
                if converted_amount:
                    print(f"{amount} {converter.base_currency} = {converted_amount:.2f} {target_currency}")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        
        elif choice == "3":
            converter.show_conversion_history()
        
        elif choice == "4":
            print("Thank you for using the Currency Exchange Rate Checker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

