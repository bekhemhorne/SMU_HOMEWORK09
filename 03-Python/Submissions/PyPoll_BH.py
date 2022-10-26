import csv
csvpath = "Instructions/PyPoll/Resources/election_data.csv" 

#define
rows = 0
votes = {}
vote_percent = {}




with open(csvpath, encoding='utf-8') as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first or skip
    csv_header = next(csvreader)
  
#Total votes, Total number of votes per candidate with percents
    for row in csvreader:
        rows += 1
        candidate = row[2]

        #Building candidate dicts
        if candidate in votes.keys():
            votes[candidate] += 1
        else:
            votes[candidate] = 1
        
    #for x in csvreader:
       # vote_percent = (rows / candidate)

        #Correct the spacing and add percentages
    
#Find the winner


#Add header and row titles
print("Election Results \n")
print("---------------\n")
print("Total Votes: " + str(rows) + "\n")
print("---------------\n")
#print(votes)
for name in votes:
    print(f"{name}: {round(votes[name]/ rows *100, 3)}% ({votes[name]})")
print("---------------\n")
max_value = max(votes, key=votes.get)
print("The winner is: " + max_value)
print("---------------\n")



#Print to text file
with open('election_results_bh.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------\n")
    text.write("Total Votes: " + str(rows) + "\n")
    text.write("---------------\n")
    text.write(str(votes) + "\n")
    text.write("---------------\n")
    #text.write("The winner is: " + winner)
    text.write("---------------\n")



