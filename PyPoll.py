# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidats who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
# Assign a variable for the file to load and the path
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
total_votes = 0
#Candidate Options
candidate_options= []
#create candidate dictionary
candidate_votes={}
#Winning Candidate and Winning Count Tracker
winning_candidate =""
winning_count = 0
winning_percentage= 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #2 Add to the total vote count
        total_votes+=1
        #Print the candidate name from each row
        candidate_name=row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #to create candidate key
            candidate_votes[candidate_name]=0  
    #to add a vote to the candidates count
        candidate_votes[candidate_name]+=1   
with open(file_to_save,"w") as txt_file:  
#print the final vote count to the terminal
    election_results=(f"\nElection Results\n" f"-------------------------\n" f"Total Votes: {total_votes:,}\n" f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        #Get the votes by candidate
        votes=candidate_votes[candidate_name]
            #Calculate the percentage
        voter_percentage = float(votes)/float(total_votes)*100
            # To do: print out each candidate's name, vote count and percentage of votes
        candidate_results =(f"{candidate_name}: {voter_percentage:.1f}% ({votes:,})\n" )
        print(candidate_results)
        txt_file.write(candidate_results)
            #Determine winnning vote count and candidate
            #Determine if the votes is greater than the winning count
        if(votes>winning_count) and (voter_percentage > winning_percentage):
                #if true then 
            winning_count=votes 
            winning_percentage=voter_percentage
                #set winning candidate equal to the candidate name
            winning_candidate = candidate_name
        winning_candidate_summary =(f"--------------------------\n" f"Winner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage: {winning_percentage:.1f}%\n" f"-----------------------------\n")
        print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
       

        

