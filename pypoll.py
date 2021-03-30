# Open the data file
# Calculate the total number of votes cast
# List the names of all candidates who received votes
# List the number of votes received per candidate
# Calculate the percentage of votes each candidate won
# Determine who won the election

# Import CSV and OS Modules
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    header = next(file_reader)
    print(header)

    # Print each row in the CSV file
    #for row in file_reader:
     #   print(row)


