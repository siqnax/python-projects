def is_valid_move(grid, row, col, number):
    """Checks if the number inputted is a valid move."""

    # Check the row for repeated number
    for x in range(9):
        if grid[row][x] == number:
            return False

    # Check the columns for repeated number
    for x in range(9):
        if grid[x][col] == number:
            return False

    # Check the 3 by 3 square for repeated number
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True


def solve(grid, row, col):
    """Solves the sudoku"""
    try:  # This handles a wrong type found in the grid

        # If we are at the last column and row, and all digits have been inputted,
        # the board is filled and the game ends
        if col == 9:
            if row == 8:
                return True

            # This takes us to the beginning of a new row when col = 9
            row += 1
            col = 0

        # Recurse the function if the cell is not empty (that it is not empty).
        if grid[row][col] > 0:
            return solve(grid, row, col + 1)

        # Try the numbers 1 - 9 in an empty slot (slot having the number 0).
        for num in range(1, 10):

            # Check if the number is valid and enter the valid number into the cell
            if is_valid_move(grid, row, col, num):

                grid[row][col] = num

                if solve(grid, row, col + 1):
                    return True

            grid[row][col] = 0

        return False

    except TypeError:
        print('Invalid input!')


grids = [[0, 0, 8, 7, 0, 4, 0, 0, 3],
         [1, 0, 7, 3, 0, 0, 2, 0, 0],
         [3, 0, 2, 0, 0, 0, 6, 0, 7],
         [0, 0, 0, 0, 0, 0, 5, 0, 0],
         [7, 0, 0, 0, 0, 5, 1, 6, 0],
         [0, 8, 0, 0, 3, 1, 0, 7, 0],
         [0, 0, 6, 0, 0, 8, 0, 0, 5],
         [4, 0, 0, 0, 5, 0, 0, 0, 0],
         [8, 5, 0, 9, 4, 0, 0, 0, 0]]


# Function to print board
def print_board():
    """Prints the sudoku board"""
    print(' Sudoku Board '.center(21, '*'))

    for i in range(9):
        for j in range(9):
            print(grids[i][j], end=' ')

            if (j + 1) % 3 == 0 and j != 8:
                print('|', end=' ')

        print()

        if (i + 1) % 3 == 0 and i != 8:
            print('---------------------')

        if i == 8:
            print('\n')


# Function call
print_board()

if solve(grids, 0, 0):
    print(' Solved Board '.center(21, '*'))

    for k in range(9):
        for l in range(9):
            print(grids[k][l], end=' ')

            if (l + 1) % 3 == 0 and l != 8:
                print('|', end=' ')

        print()

        if (k + 1) % 3 == 0 and k != 8:
            print('---------------------')

else:
    print('No Solution For This Sudoku')

