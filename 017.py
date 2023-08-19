# PROBLEM
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
# If all the numbers from 1 to 1000 one thousand inclusive were written out in words, how many letters would be used

# PSEUDO
#
# Iterate from 1 to 1000 inclusive, and store a variable called letter_count
# for each number, match it against a dictionary to get the length of the string.
# call the function recursively until the num is handled.
#
#

# Dictionary mapping numbers to their word representations
letters_in_num = {
    # Mapping single-digit and some special numbers to their words
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    # Mapping tens and multiples of ten to their words
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

# Convert a number to its word representation
def num_to_words(num):
    if num in letters_in_num:
        return letters_in_num[num]
    elif num < 100:
        # Handle numbers less than 100
        tens = num // 10 * 10
        ones = num % 10
        return letters_in_num[tens] + "-" + letters_in_num[ones]
    elif num < 1000:
        # Handle numbers from 100 to 999
        hundreds = num // 100
        remainder = num % 100
        if remainder == 0:
            return letters_in_num[hundreds] + " hundred"
        else:
            return letters_in_num[hundreds] + " hundred and " + num_to_words(remainder)
    elif num == 1000:
        # Handle the special case of 1000
        return "one thousand"

# Count the number of letters in a word
def count_letters(word):
    return len(word.replace(" ", "").replace("-", ""))

# Calculate the total letters count within a specified range
def letters_count_range(start, end):
    total_count = 0
    for num in range(start, end + 1):
        word = num_to_words(num)
        count = count_letters(word)
        total_count += count
    return total_count

# Calculate and print the total letters count for numbers from 1 to 1000
result = letters_count_range(1, 1000)
print(result)