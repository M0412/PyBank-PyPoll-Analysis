# Import modules
import csv
import os

# Path to collect data from the Resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
Date = []
ProfitLosses = []
MonthsTotal = []
ProfitLossesNetTotal = []
ProfitLossesChanges = []
GreatestProfitIncrease = []
GreatestProfitDecrease = []

# Open and read csv
with open(pybank_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = next(csv_reader)
        for row in csv_reader:
                 
                 # Populate the Date list and determine the total number of months
                 Date.append(row[0])
                 MonthsTotal = len(Date)
                 print (f"Total months: {str(MonthsTotal)}")
                 
                 # Populate the Profit/losses list and determine the net total
                 ProfitLosses.append(row[1])
                 ProfitLossesNetTotal = sum(int(ProfitLosses))
                 print (f"Total: {float(ProfitLossesNetTotal)}")

                 # Determine the greatest profit increase
                 GreatestProfitIncrease = max(ProfitLosses)

                 # Determine the greatest profit decrease
                 GreatestProfitDecrease = min(ProfitLosses)


                 
               

