#Importing depencies that allow us to create file paths & the module for reading CSV files
import os
import csv

#Making sure the correct directory
os.chdir('C:\\Users\\Gael R. Gatera\\Documents\\Data Science Boot Camp\\Homeworks\Hw 3-Python')
print (os.getcwd())

#create the variables that I will need throughout the code
input_file = "budget_data.csv"
csvpath = os.path.join('..', 'Hw 3-Python', 'budget_data.csv')
outpath = os.path.join('..', 'Hw 3-Python', 'summarybank.csv')
revenue, date = ([] for x in range(2))
row_num = 0

#reading using the CSV module
with open(csvpath, mode='r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    
    for row in reader:
        date.append(row[0])
        revenue.append(row[1])
        row_num += 1

# Procedure to creating the summary table
# creating the "financial analysis" header using the print function
print("\nFinancial Analysis", "\n")

# Step 1 creating the total months header using the print function
print("Total Months:", row_num)

# Step 2 calculating the total revenue using the print
TotalRevenue = 0
for x in revenue:
    TotalRevenue += int(x)

print("Total Revenue: $" + str(TotalRevenue))

# Step 3 Calculating the average revenue change
# First holding the total revenue change into a separate variable
totalrevenuechange = 0
for x in range(row_num):
    totalrevenuechange += int(revenue[x]) - int(revenue[x - 1])

# Creating a variable in order to remove the first revenue change and make the math accurate

accuracy = (int(revenue[0]) - int(revenue[-1]))
totalrevenuechange_adj = totalrevenuechange - accuracy

averagerevchange = (totalrevenuechange_adj + int(revenue[0])) / row_num
print("Average Revenue Change: $" + str(round(averagerevchange)))

# Step 4 calculate the greatest increase in revenue
greatest_increase = 0
for y in range(len(revenue)):
    if int(revenue[y]) - int(revenue[y - 1]) > greatest_increase:
        greatest_increase = int(revenue[y]) - int(revenue[y - 1])
        highest_month = date[y]

print("Greatest Increase in Revenue:", highest_month, "($" + str(greatest_increase) + ")")

# Step 5 calculate the greatest decrease in revenue
greatest_decrease = 0
for z in range(len(revenue)):
    if int(revenue[z]) - int(revenue[z - 1]) < greatest_decrease:
        greatest_decrease = int(revenue[z]) - int(revenue[z - 1])
        low_month = date[z]

print("Greatest Decrease in Revenue:", low_month, "($" + str(greatest_decrease) + ")")

# white space after table
print("\n\n")

# Step 6 writing on the output file
with open(outpath, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Financial Analysis for: " + input_file],
        ["-" * 50],
        ["Total Months: " + str(row_num)],
        ["Total Revenue: $" + str(TotalRevenue)],
        ["Average Revenue Change: $" + str(round(averagerevchange))],
        ["Greatest Increase in Revenue: " + str(highest_month) + " ($" + str(greatest_increase) + ")"],
        ["Greatest Decrease in Revenue: " + str(low_month) + " ($" + str(greatest_decrease) + ")"]
    ])

