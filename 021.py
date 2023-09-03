# PROBLEM
#
# Evaluate the sum of all the amicable numbers under 10000

# PSEUDO
#
# loop, factor, and sum the factors of each number.
# keep a list of the sums of factors
#  for each num, check if the list[sum] == num
# if true, add to rolling count
#

def factor(num):
    factors = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def amicable_numbers(limit):
    amicable_sum = 0
    for i in range(2, limit):
        factor_sum = sum(factor(i))
        # check if the numbers are an amicable pair, note that num cannot be amicable with itself
        if i != factor_sum and i == sum(factor(factor_sum)):
            amicable_sum += i

    return amicable_sum

print(amicable_numbers(10000))