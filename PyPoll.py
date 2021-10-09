# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidats who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
# Assig a variable for the file to load and the path
import csv
import os
#Assign a variabel to lad a file from a path
file_to_load=os.path.join("Resources","election_results.csv")
#Create a filename variable to a direct o indirect path to the file
file_to_save=os.path.join("Analysis","election_analysis.txt")
#Using the with statement open the file as a text file
## with open(file_to_save,"w") as txt_file:
    #Write some data to the file
    # txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
#Open the elction results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)

