# PROBLEM
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all numbers from 1 to 20

 # PSUEDO
 #
 # starting a num at 20, check if num has 0 modulo for all nums 1-20
 # If yes, return num, else increment num by 20

def smallest_number():
    # start checking from 20
    num = 20
    # range 2-20
    while True:
        for i in range(2, 21):
            if num % i != 0:
                # if the number is not divisible by one of the values, break the loop
                break
            if i == 20:
                # all conditions are met
                return num
        # increment the num and try again
        num += 20

print(smallest_number())


