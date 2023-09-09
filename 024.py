# PROBLEM
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# PSEUDO
#
# use Lehmer code to map the relationship of lexicographically ordered permutations of a set.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# the first permutation is n = 0, so the millionth is n = 999,999
nth = 999999
nth_permutation = ""

for i in range(9, -1, -1):
    digit = nth // factorial(i)  # Use integer division
    nth_permutation += str(set[digit])
    del set[digit]
    nth = nth % factorial(i)

print(nth_permutation)