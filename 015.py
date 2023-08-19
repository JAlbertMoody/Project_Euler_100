# PROBLEM
#
# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20 x 20 grid?

# PSEUDO
#
# This is a DP problem which requires me to start from the end and work backwards.
# Think of each intersection as a node and how many routes go from that node to the finish, moving only down and right.
# A 3x3 grid where each node is labelled with num of routes to the finish is as shown below.
# 20 - 10 - 4 - 1
# 10 - 6 - 3 - 1
# 4 - 3 - 2 - 1
# 1 - 1 - 1 - 1
# basically I need to build the pattern with loops until n = 20.

def lattice_paths(grid_size):
    # this list will hold many lists, one for each row in the grid
    grid = []
    for i in range(grid_size + 1):
        # initiate empty list for the current row.
        row = []
        for j in range(grid_size + 1):
            if i > 0 and j > 0:
                # if the previous values exist, add them together to make the new value
                row.append((grid[i-1][j]) + (row[j-1]))
            else:
                row.append(1)
        grid.append(row)
    return grid[grid_size][grid_size]

print(lattice_paths(20))