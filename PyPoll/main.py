#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import os

election_data = os.path.join("..", "election_data.csv")

election_data_df = pd.read_csv(election_data)


#Obtain total number of votes cast
total_votes = election_data_df["Voter ID"].count()
print("Election Results")
print("-"*30)
print("Total Votes: " + str(election_data_df["Voter ID"].count()))
print("-"*30)

#Obtain number of votes won for each candidate
khan_votes = (election_data_df["Candidate"]=="Khan").sum()
correy_votes = (election_data_df["Candidate"]=="Correy").sum()
li_votes = (election_data_df["Candidate"]=="Li").sum()
otooley_votes = (election_data_df["Candidate"]=="O'Tooley").sum()

#Calculate percentage of votes won for each candidate
khan_percent = khan_votes / total_votes * 100
correy_percent = correy_votes / total_votes * 100
li_percent = li_votes / total_votes * 100
otooley_percent = otooley_votes / total_votes * 100

print("Khan: ""%.3f" % khan_percent + "% " + "(" + str(khan_votes) + ")")
print("Correy: ""%.3f" % correy_percent + "% " + "(" + str(correy_votes) + ")")
print("Li: ""%.3f" % li_percent + "% " + "(" + str(li_votes) + ")")
print("O'Tooley: ""%.3f" % otooley_percent + "% " + "(" + str(otooley_votes) + ")")
print("-" * 30)

#Calculate winner of the election based on popular vote
candidate_dict= {
    "Khan": [khan_percent, khan_votes],
    "Correy": [correy_percent, correy_votes],
    "Li": [li_percent, li_votes],
    "O'Tooley": [otooley_percent, otooley_votes]
}

votesList = list(candidate_dict.values())

winner = str(list(candidate_dict.keys())[list(candidate_dict.values()).index(max(votesList))])

print("Winner: " + winner)

import subprocess
with open("PyPoll.txt", "w+") as output:
    subprocess.call(["python", "./main.py"], stdout=output);







