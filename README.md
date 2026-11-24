[README.md](https://github.com/user-attachments/files/35330488/README.md)
# CodeAlpha - Stock Portfolio Tracker

A console-based Stock Portfolio Tracker created for **CodeAlpha Python Programming Task 2**.

## Assignment requirements covered
- User enters stock symbols and quantities.
- A hardcoded Python dictionary stores sample stock prices.
- The program calculates each holding's investment value and the grand total.
- The user can optionally save the report as a CSV file.

## Project structure
```text
CodeAlpha_StockPortfolioTracker/
|-- main.py
|-- README.md
|-- .gitignore
|-- stock_portfolio/
|   |-- __init__.py
|   |-- stocks.py
|   |-- tracker.py
|   |-- file_handler.py
|-- reports/
    |-- .gitkeep
```
The `portfolio_summary.csv` file is created in `reports/` when the user chooses to save the report.

## Requirements
- Python 3.8 or newer
- VS Code (recommended)
- No external packages required; CSV uses Python's built-in `csv` module.

## Run in VS Code
1. Extract the ZIP and open the `CodeAlpha_StockPortfolioTracker` folder in VS Code.
2. Select **Terminal > New Terminal**.
3. Run:
   ```bash
   python main.py
   ```
   On some Windows installations, use `py main.py`.

## Sample stock prices
| Symbol | Sample price per share |
|---|---:|
| AAPL | $180.00 |
| TSLA | $250.00 |
| GOOGL | $140.00 |
| MSFT | $420.00 |
| AMZN | $185.00 |

**Note:** These are hardcoded example prices for this assignment, not live market prices.

## How to use
1. Enter a stock symbol from the displayed list.
2. Enter the quantity you own.
3. Add more stocks or type `DONE`.
4. Review the investment value of each stock and the grand total.
5. Enter `y` to save the CSV report, or `n` to skip.

## Source files
- `main.py`: starts the application.
- `stock_portfolio/stocks.py`: hardcoded stock-price dictionary.
- `stock_portfolio/tracker.py`: input, calculations and display.
- `stock_portfolio/file_handler.py`: CSV report saving.
- `reports/`: stores the generated CSV report.
