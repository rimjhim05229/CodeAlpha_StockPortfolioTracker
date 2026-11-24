"""Input, calculation and display functions for the tracker."""
from stock_portfolio.stocks import STOCK_PRICES
from stock_portfolio.file_handler import save_portfolio_to_csv

def get_positive_quantity(symbol):
    while True:
        try:
            quantity = int(input(f"Enter quantity of {symbol}: ").strip())
            if quantity > 0:
                return quantity
            print("Quantity must be greater than zero. Please try again.")
        except ValueError:
            print("Please enter a valid whole number, such as 5.")

def display_available_stocks():
    print("\nAvailable stocks (sample prices):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f} per share")

def display_portfolio(holdings):
    print("\n" + "=" * 58)
    print("                  YOUR STOCK PORTFOLIO")
    print("=" * 58)
    print(f'{"Stock":<12}{"Quantity":>10}{"Price/Share":>16}{"Investment":>18}')
    print("-" * 58)
    total_investment = 0.0

    for symbol, details in holdings.items():
        investment = details["quantity"] * details["price"]
        details["investment"] = investment
        total_investment += investment
        print(f'{symbol:<12}{details["quantity"]:>10}  ${details["price"]:>12,.2f}  ${investment:>14,.2f}')

    print("-" * 58)
    print(f'{"TOTAL INVESTMENT":<38}${total_investment:>17,.2f}')
    print("=" * 58)
    return total_investment

def run_tracker():
    holdings = {}
    print("\n==============================================")
    print("          STOCK PORTFOLIO TRACKER")
    print("==============================================")
    print("Enter the stock symbols you own and their quantities.")
    print("Type DONE when you have finished adding stocks.")
    display_available_stocks()

    while True:
        symbol = input("\nEnter stock symbol (or DONE to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if not symbol:
            print("Stock symbol cannot be empty.")
            continue
        if symbol not in STOCK_PRICES:
            print("Sorry, that stock is not in our price list.")
            print("Please choose one of the displayed stock symbols.")
            continue

        quantity = get_positive_quantity(symbol)
        if symbol in holdings:
            holdings[symbol]["quantity"] += quantity
        else:
            holdings[symbol] = {
                "quantity": quantity,
                "price": STOCK_PRICES[symbol],
                "investment": 0.0,
            }
        print(f"Added {quantity} share(s) of {symbol}.")

    if not holdings:
        print("\nNo stocks were added. Your portfolio is empty.")
        print("Thank you for using Stock Portfolio Tracker!")
        return

    total = display_portfolio(holdings)
    save_choice = input("\nWould you like to save this report as a CSV file? (y/n): ").strip().lower()
    if save_choice == "y":
        saved_path = save_portfolio_to_csv(holdings, total)
        print(f"Portfolio report saved successfully at: {saved_path}")
    else:
        print("Report was not saved.")
    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    run_tracker()
