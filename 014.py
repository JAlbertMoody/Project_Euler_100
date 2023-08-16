# PROBLEM
# The following iterative sequence is defined for the set of positive integers:
#   n => n/2 (n is even)
#   n => 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1.
# t can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

# PSEUDO
#
# for each num, starting at 2 and going to a million, apply collatz operations
# keep a list for the result of each operation, return len(list) once the final term is one
# keep a tally for the longest
#
# Could optimize by eliminating multiple from a dictionary to remove evens...

def longest_collatz(num):
    # tracking variables for the length of collatz and number itself
    longest_num = 0
    longest_collatz_list = 0
    for i in range(2, num):
        #  perform the operations until the number is 1
        current_num = i
        nums_list = [i]
        while i > 1:
            if i % 2 == 0:
                i = i / 2
                nums_list.append(i)
            else:
                i = (3 * i) + 1
                nums_list.append(i)
        # check if it is greater than any previous nums
        if len(nums_list) > longest_collatz_list:
            longest_collatz_list = len(nums_list)
            longest_num = current_num

    return longest_num



print(longest_collatz(1_000_000))