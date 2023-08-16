# PROBLEM
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# PSEUDO
#
# Square 2 to the 1000th power
# turn the answer into a string then iterate to sum
# return the sum

def power_digit_sum(power):
    answer_str = (str(2 ** power))
    answer = 0
    for num in answer_str:
        answer += int(num)
    return answer

print(power_digit_sum(1000))
