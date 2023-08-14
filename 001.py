# PROBLEM:
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# PSUEDO
#
# loop through all numbers from 1 to 1000
# use modulo to check if they are a multiple
# if true, append to list
# return sum of list

def multiple_of_three_and_five():
    #define an empty list to add multiples to.
    multiples = []
    # loop to range(1000) , this will be 1-999
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
            # add to list if it is a multiple.

    #use the built in sum function to return the answer
    return sum(multiples)

print(multiple_of_three_and_five())





