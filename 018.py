# PROBLEM
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:

# PSEUDO
#
# Starting at the second to last list in triangle, iterate through every value
# every value should be change to equal the largest of the sum of itself and values "below it" and "diagonally down and right"
# Once the whole triangle is iterated through, the very first list will contain the answer
#

triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

test_triangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3],
]

def maximum_path_sum(triangle):
    # start the loop from the second to last list element, looping backwards
    for i in range(len(triangle) - 2, -1, -1):
        # iterate through each element
        for j in range(len(triangle[i])):
            current = triangle[i][j]
            below = triangle[i + 1][j]
            diagonal = triangle[i + 1][j + 1]

            # update the value at the index
            triangle[i][j] = max((current + below), (current + diagonal))

    # after the loops, the first element should be the answer.
    return triangle[0][0]

print(maximum_path_sum(triangle))