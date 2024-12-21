import numpy as np

def print_grid(grid):
    print(np.matrix(grid))

def is_valid(x, y, n, grid):
    for i in range(9):
        if grid[x][i] == n:
            return False
        
    for j in range(9):
        if grid[i][y] == n:
            return False
    return True

def is_valid_neighbor(x, y, n, grid):
    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j] == n:
                return False
    return True

def sudoku():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if is_valid(x, y, n, grid):
                        grid[x][y] = n
                        if sudoku():
                            return True
                        grid[x][y] = 0
                return False
    return True

if __name__ == "__main__":
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original board")
    print_grid(grid)
    #print("Check for valid board")
    #print(is_valid(3,4,8,grid))
    #print("Check for valid neighbor")
    #print(is_valid_neighbor(3,4,8,grid))
    print("Solved board")
    if sudoku():
        print_grid(grid)
    else:
        print("No solution exists.")