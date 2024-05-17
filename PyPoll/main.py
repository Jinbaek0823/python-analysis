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