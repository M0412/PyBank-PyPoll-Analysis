# Import modules
import os
import csv 

# Path to collect data from the Resources folder
pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

# Lists to store data
Candidate_list = []
UniqueCandidatelist = []
VotesPerCandidate = []
PercentageOfVotes = []

# Open and read csv
with open(pypoll_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
                # Determine the total number of votes cast
                 TotalVotes = len(row[0])
                 print (f"Total votes: {str(TotalVotes)}")
        
        # Populate the candidate list with the candidate names invluding the header
        csv_header = next(csv_reader)
        for row in csv_reader:
                Candidate_list.append(row[2])
                UniqueCandidatelist = set(Candidate_list)

        # Returning the total number of votes each candidate won
        for candidate in UniqueCandidatelist:
                VotesPerCandidate = Candidate_list.count(candidate)  
                Winner_Candidate = max(VotesPerCandidate)
                PercentageOfVotes = (VotesPerCandidate / TotalVotes) * 100

#Printing results
print("Election Results:", "--------------------------------", f"Total Votes: {TotalVotes}", "--------------------------------", )


                


