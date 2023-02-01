'''Find the common letter found in both compartments of each rucksack.
Provide a priority number to each sack, return the total sum'''

from mimetypes import common_types
# create a list to hold the file contents
file_list = []

# open the file, read the contents into file
with open("day3.txt", "r") as file:
    for line in file:

        # remove the newline character
        line = line.replace("\n", "")

        # split each line
        line.split()

        # append each line to the file_list
        file_list.append(line)

# Create an iterator
i = 0 

# Create variable to hold total score
total_score = 0

# calculate length of file_list
file_length = len(file_list)

# loop through the file_list
while i <= (file_length - 1):

    # calculate the lenght of each line to split into upper and lower compartment
    line_length = len(file_list[i]) / 2

    # change value to integer
    line_length = int(line_length)
    
    # slice each line based of the line_length value into upper/lower compartments
    upper_compartment = file_list[i][:line_length]
    lower_compartment = file_list[i][line_length:]

    # create a list of the two compartments as set to compare
    common_type = list(set(upper_compartment)&set(lower_compartment))
    for x in common_type:

        # determine if letter is upper or lower
        # Use the ASCII value to calculate the letter priority
        if (x.islower()):
            x = ord(x) - 96
        elif (x.isupper()):
            x = x.lower()
            x = ((ord(x) - 96) * 2)
        
        # add that value to total score
        total_score += x
    
    # increase the iterator by 1
    i += 1

# print the total ASCII score value
print(total_score)  




