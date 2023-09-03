# PROBLEM
#
# Find the sum of the digits in the number 100!

# PSEUDO
#
# create a loop to loop through down from the num to 0
# keep a rolling number that is the factorials multiplicand
# turn that num into a string, iterate through it, add the elements together for the answer
#

def factorial(num):
    answer = num
    for i in range(num - 1, 1, -1):
        answer *= i
    return answer

def sum_of_num(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

def factorial_digit_sum(num):
    return sum_of_num(factorial(num))

# print(factorial(10))
# print(sum_of_num(12))
print(factorial_digit_sum(100))