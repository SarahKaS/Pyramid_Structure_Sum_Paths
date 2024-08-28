# Load data
# We will choose here to not use numpy, but computing results with vectors can simplify the code

with open('input.txt', 'r') as file:
    pyramid = [[int(num) for num in line.split()] for line in file]
# print(pyramid)

# Parameters initialization:
totrows = len(pyramid)
totcol = len(pyramid[-1])
tot_num_in_line = totrows - 1
sum_vec = []
all_sums = 0

""" 
The Take_all_values_init function adds two "child" numbers to their parent and keep the 2 vectors created
We will take all the number from bottom to top,
So our first count will be one row before the last one 
"""

# For the bottom line only (first sum):
def Take_all_values_init(pyra, tot_num_in_line):
    count_line = 1
    i = tot_num_in_line - 1

    for j in range(tot_num_in_line):
        right_sum = pyra[i+1][j] + pyra[i][j]
        left_sum = pyra[i+1][j+1] + pyra[i][j]
        sum_vec.append(right_sum)
        sum_vec.append(left_sum)
        # print(sum_vec)
    i -= 1
    return Take_all_values(pyra, sum_vec, i, count_line)


""" 
The Take_all_values function works the same way as the init function, but this time we will use the whole sum_vector instead of the "child" numbers
"""
# For all the other counts (second line from bottom and up):
def Take_all_values(pyra, sum_vec, tot_num_in_line, count):
    new_vec = []
    sum_local = 0
    count_l = count + 1

    i = tot_num_in_line

    for j in range(tot_num_in_line+1):
        left_indx = j*(2**(count))
        right_indx = (j+2)*(2**(count))
        for k in range(left_indx,right_indx): # take only the relevant values from the sum vector
            sum_local = sum_vec[k] + pyra[i][j]
            new_vec.append(sum_local)
        # print(new_vec)

    if i == 0:
        # print("We got the vector of all the sums:\n{}".format(new_vec))
        return(new_vec)

    i -= 1
    return Take_all_values(pyra, new_vec, i, count_l)



# Use the init function that will send us to the general function after summing the bottom line:
all_sums = Take_all_values_init(pyramid, tot_num_in_line)



"""
# simple result check for our input (18 lines in total):
print(len(all_sums)))
print(2**(18-1))
"""




"""
Now let's count the values and range them according to the count using Counter:
We will get a dictionary with sum:occurrence for each sum
"""

from collections import Counter
print("Sum  |  Count")
values = []
keys = []



count_sums = Counter(all_sums)
sum_dic_ranged = count_sums.most_common() # the most_common() method will range the values in DESC order

# We will print the result here and export it to an output.txt file
with open('output.txt', 'w') as f:
    f.write("Sum  |  Count\n")
    for keys, values in sum_dic_ranged:
        f.write("{}  |  {}\n".format(keys, values))
        print("{}  |  {}".format(keys, values))




