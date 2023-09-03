# PROBLEM
#
# a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# What is the total of all the name scores in the file?

# PSEUDO
#
# create a dictionary for letters and their scores for reference
# import file and manipulate it into a list
# sort it alphabetically
# perform the arithmatic

alphabet_dict = {}

# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Populate the dictionary with letter-to-number mappings
for index, letter in enumerate(alphabet, start=1):
    alphabet_dict[letter] = index

# Print the alphabet dictionary
print(alphabet_dict)

with open("names.txt", "r") as file:
    # Read the content of the file and store it in a variable, and process it
    names_content = file.read().split(',')
    name_list = [name.strip('"') for name in names_content]
    sorted_list = sorted(name_list)
    # set the rolling score to zero
    names_scores = 0

    for index, name in enumerate(sorted_list, start=1):
        # for each name find out its total letters score and multiply by it's index
        current_score = 0
        for letter in name:
            current_score += alphabet_dict[letter.lower()]
        current_score *= index
        # add to rolling score
        names_scores += current_score

    print(names_scores)


