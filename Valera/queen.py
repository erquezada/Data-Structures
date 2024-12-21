import numpy as np

def print_grid(grid):
    for row in grid:
        print(' '.join(['1' if x == 1 else '0' for x in row]))

def is_valid(grid, x, y, N):
    # Check the row and column for conflicts
    for i in range(N):
        if grid[x][i] == 1 or grid[i][y] == 1:
            return False
    
    # Check the upper-left diagonal
    i, j = x, y
    while i >= 0 and j >= 0:
        if grid[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = x, y
    while i >= 0 and j < N:
        if grid[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(N):
    grid = np.zeros((N, N), dtype=int)

    def solve(row):
        if row == N:
            print_grid(grid)
            return True

        for col in range(N):
            if is_valid(grid, row, col, N):
                grid[row][col] = 1
                if solve(row + 1):
                    return True
                grid[row][col] = 0  # Backtrack if no solution found

        return False

    if not solve(0):
        print("No solution exists")

# Example usage:
solve_n_queens(8)  # Solve for an 8x8 chessboard


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Test is_valid with custom coordinates (0, 1)
    print(is_valid(grid, 0, 1, len(grid)))  # Should print True or False