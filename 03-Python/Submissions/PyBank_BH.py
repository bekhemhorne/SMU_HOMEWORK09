
import csv

from sympy import N

csvpath = "PyBank/Resources/budget_data.csv"

rows = 0
total = 0

tot_changes = 0
num_changes = 0 #expected 85
last_profit = 0

# think of a code to not use high values
max_change = -999999
min_change = 999999
min_month = ""
max_month = ""






with open(csvpath, encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')   

    csv_header = next(csvreader)
    

     
    for row in csvreader:

        rows += 1
        total += int(row[1])

        #Calc the changes
        if rows == 1:
            last_profit = int(row[1])
        else:
            change = int(row[1]) - last_profit
            tot_changes += change
            num_changes += 1

            #Find max/min of changes
            if (change > max_change):
                max_change = change
                max_month = row[0]
            elif (change < min_change):
                min_change = change
                min_month = row[0]
            else:
                pass

            #Add Header and titles to rows


            #reset
            last_profit = int(row[1])


#Print statements
print("Financial Analysis\n")
print("------------------------\n")
print("Total Months: " + str(rows) + "\n")
print("Total: " + str(total) + "\n")
print(f"Average Change: {tot_changes / num_changes}" + "\n")
print(f"Greatest Increase in Profits: {max_month}: {max_change}" + "\n")
print(f"Greatest Decrease in Profits: {min_month}: {min_change}" + "\n")


#Print to text file
with open('financial_analysis_BH.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------------\n")
    text.write("Total Months: " + str(rows) + "\n")
    text.write("Total: " + str(total) + "\n")
    text.write(f"Average Change: {tot_changes / num_changes}" + "\n")
    text.write(f"Greatest Increase in Profits: {max_month}: {max_change}" + "\n")
    text.write(f"Greatest Decrease in Profits: {min_month}: {min_change}" + "\n")



