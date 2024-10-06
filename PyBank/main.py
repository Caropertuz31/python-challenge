# PyBank Analysis Script

# Dependencies
import os  # For file path operations
import csv  # For reading CSV files

# Path to load and output the files
csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "financial_analysis.txt")

# Define variables to track the financial data and store our calculations
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Open and read the CSV file
with open(csvpath, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract date and profit/loss from the current row
        date = row[0]
        profit = int(row[1])

        # Increment total months
        total_months += 1

        # Add to net total
        net_total += profit

        # Calculate change in profit (skip for the first row)
        if total_months > 1:
            change = profit - previous_profit
            profit_changes.append(change)

            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Update previous profit for the next iteration
        previous_profit = profit

# Calculate average change
average_change = sum(profit_changes) / len(profit_changes)

# Prepare the analysis results
analysis = f"""Financial Analysis
----------------------------
Total Months in the dataset: {total_months}

The net total amount of "Profit/Losses" over the entire period: ${net_total}

Average Change: ${average_change:.2f}

Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})

Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})
"""

# Print the analysis to the console
print(analysis)

# Write the analysis to a text file
with open(output_path, 'w') as file:
    file.write(analysis)

print(f"Analysis has been saved to {output_path}")





