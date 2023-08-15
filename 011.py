# PROBLEM
#
# In the 20 by 20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20 by 20 grid?

# PSEUDO
#
# Construct a list of lists, iterate through every node(value)
# For each node(value) search right, down, horizontal down right, and horizontal down left.
# Each node, searching for each four, should render every single combination.

# Taking data from the website and turning each row into a list.
r1_str = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
r1 = [int(num) for num in r1_str.split(' ')]

r2_str = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'
r2 = [int(num) for num in r2_str.split(' ')]

r3_str = '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'
r3 = [int(num) for num in r3_str.split(' ')]

r4_str = '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'
r4 = [int(num) for num in r4_str.split(' ')]

r5_str = '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'
r5 = [int(num) for num in r5_str.split(' ')]

r6_str = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
r6 = [int(num) for num in r6_str.split(' ')]

r7_str = '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'
r7 = [int(num) for num in r7_str.split(' ')]

r8_str = '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'
r8 = [int(num) for num in r8_str.split(' ')]

r9_str = '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'
r9 = [int(num) for num in r9_str.split(' ')]

r10_str = '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'
r10 = [int(num) for num in r10_str.split(' ')]

r11_str = '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'
r11 = [int(num) for num in r11_str.split(' ')]

r12_str = '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'
r12 = [int(num) for num in r12_str.split(' ')]

r13_str = '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'
r13 = [int(num) for num in r13_str.split(' ')]

r14_str = '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'
r14 = [int(num) for num in r14_str.split(' ')]

r15_str = '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'
r15 = [int(num) for num in r15_str.split(' ')]

r16_str = '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'
r16 = [int(num) for num in r16_str.split(' ')]

r17_str = '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'
r17 = [int(num) for num in r17_str.split(' ')]

r18_str = '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'
r18 = [int(num) for num in r18_str.split(' ')]

r19_str = '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'
r19 = [int(num) for num in r19_str.split(' ')]

r20_str = '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
r20 = [int(num) for num in r20_str.split(' ')]

# compiling the data into a list of lists that we can now work with.
grid = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

def find_greatest_product(grid):
    # intiate a variable at zero to keep track of the answer
    largest_product = 0
    for i in range(20):
        for j in range(20):
            # print(grid[i][j])
            # set products to 0 at every iteration.
            products = [0]
            # Search right if it exists
            if j < 17:
                products.append(grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3])
            # Search down if it exists
            if i < 17:
                products.append(grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j])
            # Search down and right if it exists
            if j < 17 and i < 17:
                products.append(grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3])
            # Search down and left if it exists
            if 3 < j and i < 17:
                products.append(grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3])

            # check if the largest of the four searches on the num is greater than the largest on record.
            # if it is, that is the new value.
            if max(products) > largest_product:
                largest_product = max(products)

    return largest_product



print(find_greatest_product(grid))