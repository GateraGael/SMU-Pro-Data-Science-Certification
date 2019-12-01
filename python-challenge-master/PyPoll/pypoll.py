#Importing dependencies that allow us to create file paths & module for reading csv files
import os
import csv

#Making sure that I'm in the correct directory
os.chdir('C:\\Users\\Gael R. Gatera\\Documents\\Data Science Boot Camp\\Homeworks\Hw 3-Python')
print (os.getcwd())

#create the higher level variables that I will need throughout the code 
input_file = 'election_data.csv'
csvpath = os.path.join('..', 'Hw 3-Python', 'election_data.csv')
outpath = os.path.join('..', 'Hw 3-Python', 'summaryelections.csv')
candidates, total_candidates, candidate_perc, candidate_total, summaries = ([] for i in range(5))


#Reading the file using the csv module
with open(csvpath, mode='r', newline='') as elections_data:
    reader = csv.reader(elections_data, delimiter=',')
    next(reader)

    num_rows = 0
#Making sure it is 2 for third column 
    for row in reader:
        total_candidates.append(row[2])
        num_rows += 1

# Making sure the list of total candidates is organized
candidates_sorted = sorted(total_candidates)


for x in range(num_rows):
    if candidates_sorted[x - 1] != candidates_sorted[x]:
        candidates.append(candidates_sorted[x])

# Procedure to create the summary table
# Step 1 creating the "Election Results" & "Total Votes" headers using the print function

print("\nElection Results")
print("Total Votes:", num_rows)

# Step 2 counting the candidates

for y in range(len(candidates)):
    candidate_count = 0
    for z in range(len(candidates_sorted)):
        if candidates[y] == candidates_sorted[z]:
            candidate_count += 1

# Step 3 Calculating the vote percentage of each candidate and appending to associated name 
    candidate_perc.append(round(candidate_count/ num_rows * 100, 1))
    candidate_total.append(candidate_count)

# Found the zip function which aggregates elements and used it to put together the data of each candidate
candidate_data = zip(candidates, candidate_perc, candidate_total)
for row in candidate_data:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summaries.append(summary)

# Step 4 comparing the total votes of each candidate and printing winner 
for z in range(len(candidate_perc)):
    if candidate_total[z] > candidate_total[z - 1]:
        winner_name = candidates[z]

print("Winner:", winner_name)
print("\n\n")

#Step 5 Writing to outputfile
with open(outpath, mode='w', newline='') as summaries_data:
    writer = csv.writer(summaries_data)

    writer.writerows([
        ["Election Results for: " + input_file],
        ["Total Votes: " + str(num_rows)],
    ])
    writer.writerows(summaries)
    writer.writerows([
        ["Winner: " + str(winner_name)],
    ])
