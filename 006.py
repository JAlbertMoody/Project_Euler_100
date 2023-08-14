# PROBLEM
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# PSEUDO
#
# iterate and add i**2 to i == 100
# iterate and add 1-100, then square
# do the iteration in one for loop to be efficient
# subtract one from the other and return answer

def sum():
    sum_of_squares = 0
    sum_of_naturals = 0
    # iterate from 1 to 100
    for i in range(1, 101):
        # add the squared value to the count
        sum_of_squares += (i**2)
        # add the natural value to the count
        sum_of_naturals += i
    return (sum_of_naturals**2)-sum_of_squares

print(sum())



