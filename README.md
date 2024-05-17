# python-challenge
# python-challenge

1. Py Bank
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




2. Py Poll
import csv

py_poll = "/Users/bbjinjin/Desktop/Data_BootCamp/HomeWork/Module 3 Homework/python-challenge/PyPoll/Resources/election_data.csv"


candidate_votes = {}
total_votes = 0

with open(py_poll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
   
    for row in csvreader:
     
        total_votes += 1
        candidate_name = row[2]
        
        
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
      
        else:
            candidate_votes[candidate_name] += 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")


for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

print("-------------------------")

winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")


with open("/Users/bbjinjin/Desktop/Data_BootCamp/HomeWork/Module 3 Homework/python-challenge/PyPoll/Analysis/analysis.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")
