# PROBLEM
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers

# PSEUDO
#
# brute force problem
# have a seperate function to check if is palindrome
# turn into string, check if it equals it's revers
#
# left val, right val. right val decrease from 999 down to 900
# left val decrease by 1 if not found.
#  check if found in every iterationg.

def is_palindrome(num):
    string = str(num)
    if string == string[::-1]:
        return True
    else:
        return False

# print(is_palindrome(60006))

def brute_force():
    # initiate our two nums
    num1 = 999
    num2 = 999
    # double loop to check 999 w/ 999-900, 998 w/ 998-900, ...
    for i in range(num1, 900, -1):
        for j in range(num1, 900, -1):
            product = num1 * num2
            # check if the combo is a palindrome, return if so
            if is_palindrome(product):
                print(num1, num2)
                return(product)
            # not a palindrome, iterate num 2 down
            num2 -= 1

        num1 -= 1
        # not in that set of combinations, iterate num1 down
        num2 = num1
        # set num2 equal to num 1 to minimize duplicate combinations.
        # loop through again.

print(brute_force())



# making sure i set up the double loop correctly
def test_loop():
    num1 = 5
    num2 = 5
    for i in range(num1, 0, -1):
        for j in range(num1, 0, -1):
            print(num1, num2)
            num2 -= 1
        num1 -= 1
        num2 = num1

# test_loop()



# short answer "maximum([x * y for x = 1:999 for y = 1:999 if reverse(digits(x*y)) == digits(x*y)])"
