## Create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


# Import dependencies

import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables

voters_candidates = []
votes_per_candidate = []

# Create path to collect data from the Resources folder

election_data_csv = r"C:\Users\mraza\Repository\python-challenge\PyPoll\Resources\election_data.csv"

# Open and read csv

with open(election_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for i in csv_reader:

        voters_candidates.append(i[2])

    # Sort by ascending order

    sorted_list = sorted(voters_candidates)

    # Arrange the sorted list by most common outcomes

    arrange_list = sorted_list

    #count and append the votes per candidate in most common outcome order 

    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points

    for item in votes_per_candidate:
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')

print("Election Results")

print("-------------------------")

print(f"Total Votes:  {sum(count_candidate.values())}")

print("-------------------------")

print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")

print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")

print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")

print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")

print("-------------------------")

print(f"Winner:  {votes_per_candidate[0][0][0]}")

print("-------------------------")

# Export a text file with the results

with open('election_results.txt', 'w') as text:

    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    text.write("-------------------------\n")
    text.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    text.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    text.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    text.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    text.write("-------------------------\n")
    text.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    text.write("-------------------------\n")  