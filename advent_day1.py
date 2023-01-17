#create empty list to hold the file contents, starting at index 0
file_list = [[]]

# variable to store the current index of file_list
cur_index = 0

# read the file
with open("day1.txt", "r") as f:
    for line in f:
        # remove the newline character, replace with whitespace
        line = line.replace("\n", "")

        # if the next line in the file is whitespace
        if (line == ""):

            # add a empty list to file_list
            file_list.append([])

            # add 1 to the current index, so the next line from the file can be added to a file_list[i][0]
            cur_index += 1
            continue
        else:
            # add the next line from the file to the current index of the file_list
            file_list[cur_index].append(line)


# create a list to hold the total of each index in file_list
sum_file_list = [[]]

# reset current index to 0 for sum_file_list
cur_index = 0

# create iterators
i = 0
j = 0

# create list_total variable to hold sum of all elements in each sub-list
list_total = 0

# loop through the outer list level of file_list
while i <= (len(file_list) -1):

    # loop through each element at file_list[i]
    while j < len(file_list[i]):

        # add value of file_list[i][j] to list_total
        list_total += int(file_list[i][j])
        j += 1
    
    # when all elements have been counted in file_list[i], reset iterator to 0
    i += 1

    # add a blank list to sum_file_list for the next index
    
    sum_file_list.append([])

    # add the list total to the current index of sum_file_list
    sum_file_list[cur_index].append(list_total)

    # reset the list_total
    list_total = 0

    # add one to the current index
    cur_index += 1
    
    # reset the element increment variable for the next sub-list
    j = 0

# remove the empty list added at the end
sum_file_list.pop()

# sort list to find elf with most carried calories
sum_file_list.sort()

# print the list
print(type(sum_file_list[-1]))

'''PART 2
Return the total number of calories carried by the top 3 elves'''

# pull the last 3 elements from the sorted sum_file_list
top_3 = sum_file_list[-1] + sum_file_list[-2] + sum_file_list[-3]

# add the three elements together
print(sum(top_3))