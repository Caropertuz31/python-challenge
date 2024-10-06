# PyPoll Analysis Script

# Import necessary modules
import os  # For file path operations
import csv  # For reading CSV files

# Set the path for the files to load and output
csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "election_results.txt")

# Initialize variables to track the election data and store our calculations
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Open and read the CSV file
with open(csvpath, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract the candidate name from the current row
        candidate = row[2]

        # Increment total votes
        total_votes += 1

        # Update vote count for the candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        # Update the winner if this candidate has more votes
        if candidates[candidate] > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = candidates[candidate]

# Calculate vote percentages for each candidate
percentages = {name: (votes / total_votes) * 100 for name, votes in candidates.items()}

# Prepare the analysis results
analysis = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

for candidate, votes in candidates.items():
    analysis += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"

analysis += f"""-------------------------
Winner: {winner['name']}
-------------------------
"""

# Print the analysis to the console
print(analysis)

# Write the analysis to a text file
with open(output_path, 'w') as file:
    file.write(analysis)

print(f"Election results have been saved to {output_path}")