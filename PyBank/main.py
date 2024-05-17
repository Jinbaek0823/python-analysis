import os
import csv

py_bank = "/Users/bbjinjin/Desktop/Data_BootCamp/HomeWork/Module 3 Homework/python-challenge/PyBank/Resources/budget_data.csv"

total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

with open(py_bank) as csvfile:
    csv_reader = csv.reader(csvfile)

    next(csv_reader)

    for row in csv_reader:
        total_months += 1
        profit_loss = int(row[1])
        net_total += profit_loss
        change = profit_loss - previous_profit_loss
        profit_loss_changes.append(change)
        previous_profit_loss = profit_loss
        dates.append(row[0])

total_change = sum(profit_loss_changes[1:])
average_change = total_change / (total_months -1)

greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)

greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_file = "/Users/bbjinjin/Desktop/Data_BootCamp/HomeWork/Module 3 Homework/python-challenge/PyBank/Analysis/analysis.txt"
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")




