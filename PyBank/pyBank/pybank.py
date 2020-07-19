
## Challenge 1: PyBank

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 

# [budget_data.csv](PyBank/Resources/budget_data.csv). 

# The dataset is composed of two columns: `Date` and `Profit/Losses`. 

#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#*       1.	The total number of months included in the dataset

#       2.	The total net amount of "Profit/Losses" over the entire period

#       3.	The average change in "Profit/Losses" between months over the entire period

#       4.	The greatest increase in profits (date and amount) over the entire period

#       5.	The greatest decrease in losses (date and amount) over the entire period


# Import dependencies

import os

import csv

# Define PyBank's variables

months = []
profit_loss_changes = []
count_months = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0
net_profit_loss = 0

# Create the path to collect data from the Resources folder

budget_data_csv = r"C:\Users\mraza\Repository\python-challenge\PyBank\Resources\budget_data.csv"

# Open and read csv

with open(budget_data_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first

    csv_header = next(csvfile)
     
    for row in csv_reader:

        # Count of months

        count_months += 1

        # calculate net total amount of "Profit/Losses" over the entire period

        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue
        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # append each month to the months[]

            months.append(row[0])

            # append each profit_loss_change to the profit_loss_changes

            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop

            previous_month_profit_loss = current_month_profit_loss

    #calculate sum and average of the changes in "Profit/Losses" over the entire period

    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # calculate highest and lowest changes in "Profit/Losses" over the entire period

    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month

    best_month =months[highest_month_index]
    worst_month= months[lowest_month_index]

# -->>  Print the analysis to the terminal

print("Financial Analysis")

print("----------------------------")

print(f"Total Months:  {count_months}")

print(f"Total:  ${net_profit_loss}")

print(f"Average Change:  ${average_profit_loss}")

print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")

print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Export a text file with the results

with open('financial_analysis.txt', 'w') as text:

    text.write("----------------------------------------------------------\n")

    text.write("  Financial Analysis"+ "\n")

    text.write("----------------------------------------------------------\n\n")

    text.write("    Total Months: " + str(count_months) + "\n")

    text.write("    Total Profits: " + "$" + str(net_profit_loss) +"\n")

    text.write("    Average Change: " + '$' + str(int(average_profit_loss)) + "\n")

    text.write("    Greatest Increase in Profits: " + str(best_month) + " ($" + str(highest_change) + ")\n")

    text.write("    Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(lowest_change) + ")\n")

    text.write("----------------------------------------------------------\n")
