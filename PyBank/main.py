# Import modules
import csv
import os

# Path to collect data from the Resources folder and export results
pybank_csv = os.path.join("Resources", "budget_data.csv")
pybank_export = os.path.join("Analysis", "Financial_Analysis.txt")

# Open and read csv including the header
with open(pybank_csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_header = next(csv_reader)

        # Create lists and variables to store data
        MonthsTotal = 0
        ProfitLossesNetTotal = 0
        InitialChange = 0
        ProfitLossesChanges = []
        MonthName = []
        HighestProfitIncrease = ["",0]
        HighestProfitDecrease = ["", 1000000000]
        
        for row in csv_reader:
                 
                 # Populate the Date list and determine the total number of months
                 MonthsTotal += 1
                 
                 # Determine the net total
                 ProfitLossesNetTotal += int(row[1])

                 # Determine changes in profit/losses and add data to a list
                 MonthlyDiff = int(row[1]) - InitialChange
                 ProfitLossesChanges.append(MonthlyDiff)
                 MonthName.append(row[0]) 
                 InitialChange = int(row[1]) 

                 # Determine the greatest profit increase
                 if MonthlyDiff > HighestProfitIncrease[1]:
                         HighestProfitIncrease[0] = row[0]
                         HighestProfitIncrease[1] = MonthlyDiff
                
                 # Determine the greatest profit decrease
                 if MonthlyDiff < HighestProfitDecrease[1]:
                         HighestProfitDecrease[0] = row[0]
                         HighestProfitDecrease[1] = MonthlyDiff

# Determine the average of the monthly changes
ProfitLossesChanges.pop(0)
MonthlyChangesAverage = sum(ProfitLossesChanges) / len(ProfitLossesChanges) 

# Variable to store results
Output = (f"Financial Analysis\n"
          
           "----------------------------\n"
           
           f"Total Months: {MonthsTotal}\n"
           
           f"Total: ${ProfitLossesNetTotal}\n"
           
           f"Average Change: ${MonthlyChangesAverage: .2f}\n"
           
           f"Greatest Increase in Profits: {HighestProfitIncrease[0]} ${HighestProfitIncrease[1]}\n"
           
           f"Greatest Decrease in Profits: {HighestProfitDecrease[0]} ${HighestProfitDecrease[1]}\n")
                 
# Print results in terminal
print (Output)

# Export results to the text file
with open(pybank_export, "w") as txt_output:
        txt_output.write(Output)

                 




                 
               

