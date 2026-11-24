"""Save portfolio details to a CSV file."""
import csv
from pathlib import Path

def save_portfolio_to_csv(holdings, total_investment):
    project_folder = Path(__file__).resolve().parent.parent
    reports_folder = project_folder / "reports"
    reports_folder.mkdir(exist_ok=True)
    file_path = reports_folder / "portfolio_summary.csv"

    with file_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock Symbol", "Quantity", "Price per Share (USD)",
                         "Total Investment (USD)"])
        for symbol, details in holdings.items():
            writer.writerow([
                symbol, details["quantity"], f'{details["price"]:.2f}',
                f'{details["investment"]:.2f}'
            ])
        writer.writerow([])
        writer.writerow(["", "", "Grand Total (USD)", f"{total_investment:.2f}"])
    return file_path
