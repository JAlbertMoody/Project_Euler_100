# PROBLEM
#
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number
# would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that $28$ is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# PSEUDO
#
# Start generating natural numbers and triangle numbers. Have two variable to track them
# factor each number, create a list of the factors
# if the length of the factors list is greater than 500, return the number
#

def factor(num):
    # start the factors list with 1 and itself
    factors = [1, num]
    # well check if the num is divisible by 2 to start and go from there
    a = 2
    b = num / 2
    # as we factor a number a will approach b, if a is equal or greater than b, the number is fully factored out
    while b > a:
        # check if a is a factor of the number
        if num % a == 0:
            # find a's corresponding factor pair and add it to the factors list
            b = int(num / a)
            factors.append(a)
            factors.append(b)
        a += 1
    return(factors)

def triangle_nums():
    # i will be the rolling sum of natural numbers (triangular number)
    i = 0
    # j will be the current natural number
    j = 1
    # Search until a triangle has more than 500 factors.
    while True:
        i += j
        j += 1
        if len(factor(i)) > 500:
            return i

print(triangle_nums())



