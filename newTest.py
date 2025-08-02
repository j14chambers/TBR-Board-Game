import csv
import TestFiles


#fieldnames = ['Prompt', 'Title', 'Author'] # Define the order of columns

with open('output_dict.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writeheader() # Writes the header row
    writer.writerow([TestFiles.random_space_picked, TestFiles.book_title, TestFiles.book_author]) # Writes the data rows

