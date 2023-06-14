# Import modules
import os
import csv 

# Path to collect data from the Resources folder and export results
pypoll_csv = os.path.join("Resources", "election_data.csv")
pypoll_export = os.path.join("Analysis", "Election_Results.txt")

# Lists and variables to store data
Candidate_list = []
UniqueCandidatelist = []
VotesPerCandidate = []
PercentageOfVotes = []
TotalVotes = 0
HighestVotes = 0

# Open and read csv including the header
with open(pypoll_csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_header = next(csv_reader)

        for row in csv_reader:

                # Determine the total number of votes cast
                TotalVotes += 1
                
                # Populate the candidate list with the candidate names 
                Candidate_list.append(row[2])
                UniqueCandidatelist = set(Candidate_list)
                
                # Return the total number of votes each candidate won and percentage
                for candidate in UniqueCandidatelist:
                        VotesPerCandidate = Candidate_list.count(candidate)
                        PercentageOfVotes = float(VotesPerCandidate) / float(TotalVotes) * 100

                        # Determine the winner 
                        if (VotesPerCandidate > HighestVotes):
                                HighestVotes = VotesPerCandidate
                                Winner = candidate        
                        
                        # Variable to store results
                        Output = (f"Election Results:\n"
                                  "--------------------------------\n"
                                  f"Total Votes: {TotalVotes}\n"
                                  "--------------------------------\n"
                                  f"{candidate}: {PercentageOfVotes:.3f}% ({VotesPerCandidate})\n"
                                  "--------------------------------\n"
                                  f"Winner: {Winner}\n"
                                  "--------------------------------\n")
        
        # Print results in terminal
        print(Output)

# Export results to the text file
with open(pypoll_export, "w") as txt_output:
        txt_output.write(Output)



        


