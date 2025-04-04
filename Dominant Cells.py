'''
Problem Statement:
You are given a 2-dimensional grid of integers with n rows and m columns. A cell is called a dominant cell if it has a strictly greater value than all of its neighboring cells.

Neighbors are the cells that share a common side or corner with the given cell, meaning a cell can have up to 8 neighbors.

Task: Find the number of dominant cells in the grid.

Function Description:
Complete the function numCells which has the following parameter:

grid[n][m]: A 2-dimensional array of integers.

Output:
Return the number of dominant cells in the grid.

'''

def numCells(grid):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    dominant_count = 0  # Counter for dominant cells

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]  # Current cell value

            # Collect all valid neighbors
            neighbors = [
                grid[x][y]                         # Add neighbor value
                for x in range(max(0, i-1), min(rows, i+2))  # Row range (within bounds)
                for y in range(max(0, j-1), min(cols, j+2))  # Column range (within bounds)
                if (x, y) != (i, j)               # Exclude the current cell itself
            ]

            # If the current cell is greater than all its neighbors
            if all(cell > neighbor for neighbor in neighbors):
                dominant_count += 1  # Count it as a dominant cell

    return dominant_count  # Return the total number of dominant cells

# Example usage
grid = [
    [5, 3, 4],
    [1, 6, 2],
    [7, 8, 9]
]

print(numCells(grid))  # Output: 1
