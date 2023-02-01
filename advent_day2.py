"""First column = What your oponent is going to play
   Second column = What yhou should play
   A & X = Rock
   B & Y = Paper
   C & Z = Scissors
   
   Points - 1 for Rock, 2 for Paper, 3 for Scissors
            0 if you lose, 3 if a draw, 6 for a win
            Total round score - add round result plus what item you choose
            
Need to calculate what your point score would be for entire strategy guide."""

import re

# Create empty list to hold file contents as a list
file_list =[[]]

# Create variable to hold the current index of file_list
cur_index = 0

# read the file
with open("day2.txt", "r") as f:
    for line in f:
        # remove the newline character, replace with whitespace
        line = line.replace("\n", "")

        # split each line by comma
        line.split(", ")

        # add an new empty list inside the list
        file_list.append([])

        # increase the current index by 1
        cur_index += 1

        # add the file contents to the list at the current index.
        file_list[cur_index].append(line)
        
# reset cur_index
cur_index = 0


# TODO: Calculate each round
    # Need to check each list index grouping of letters (need a loop), calculate what item was chosen and, results of match.

# create a list of the possible game combinations.
game_guide = [['A X'], ['A Y'], ['A Z'], ['B X'], ['B Y'], ['B Z'], ['C X'], ['C Y'], ['C Z']]

# create a list of the possible game scores
game_points = [4, 8, 3, 1, 5, 9, 7, 2, 6]

# create a variable for total score
total_score = 0

# create iterators
i = 0
j = 0

# lenght of file list
count = len(file_list)

# loop through the file list
while i <= (count -1):

    # if the the element at file_list[i] is in game_guide list
    if file_list[i] in game_guide:
        
        # store the index value of the game_guide that matches the file_list
        j = game_guide.index(file_list[i])

        # determing the number of points to be added by looking up the value at game_points[j]
        added_points = game_points[j]

        # add the points to the total score
        total_score += added_points

        # reset the index value of the game_guide
        j = 0
    
    # increase the iterator value
    i += 1

# return the total score
print(total_score)


'''The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: 
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"'''



# create a list of the possible game combinations.
game_guide = [['A X'], ['A Y'], ['A Z'], ['B X'], ['B Y'], ['B Z'], ['C X'], ['C Y'], ['C Z']]

# create a list of the possible game scores
game_points_2 = [3, 4, 8, 1, 5, 9, 2, 6, 7]

# create a variable for total score
total_score = 0

# create iterators
i = 0
j = 0

# lenght of file list
count = len(file_list)

# loop through the file list
while i <= (count -1):

    # if the the element at file_list[i] is in game_guide list
    if file_list[i] in game_guide:
        
        # store the index value of the game_guide that matches the file_list
        j = game_guide.index(file_list[i])

        # determing the number of points to be added by looking up the value at game_points[j]
        added_points = game_points_2[j]

        # add the points to the total score
        total_score += added_points

        # reset the index value of the game_guide
        j = 0
    
    # increase the iterator value
    i += 1

# return the total score
print(total_score)