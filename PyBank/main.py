#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os

budget_data = os.path.join("..", "budget_data.csv")

budget_data_df = pd.read_csv(budget_data)


print("Financial Analysis")
print("-"*30)
#Calculate total number of months
print("Total Months: " + str(budget_data_df["Date"].count()))
#Calculate net amount of Profit/Losses over the entire period
print("Total: $" + str(budget_data_df["Profit/Losses"].sum()))

#Create a new column to calculate average change in Profit/Losses between months
budget_data_df["shifted_column"] = budget_data_df["Profit/Losses"].shift(1)
#Obtain the difference to perform average change
budget_data_df["difference"] = budget_data_df["Profit/Losses"] - budget_data_df["shifted_column"]

#Obtain average change
average = budget_data_df["difference"].mean()
#Obtain maximum to display the greatest increase in profits
maximum = budget_data_df["difference"].max()
#Obtain minimum to display the greatest decrease in losses
minimum = budget_data_df["difference"].min()

print("Average Change: $" + "%.2f" % average)
print("Greatest Increase in Profits: Feb-2012 ($" + "%.0f" % maximum + ")")
print("Greatest Decrease in Profits: Sept-2013 ($" + "%.0f" % minimum +")")


import subprocess
with open("PyBank.txt", "w+") as output:
    subprocess.call(["python", "./main.py"], stdout=output);

