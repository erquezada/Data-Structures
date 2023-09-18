# Sudoku Problem Solver
# This program aims to solve the sudoku problem

# Leobardo Valera
# Sep 01 2023

import numpy as np

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# print(np.matrix(grid))
backtracking = 0

##############################################

def is_valid(x,y,n):
    for j in range(9):
        if grid[x][j]==n:
            return False
        
    for i in range(9):
        if grid[i][y] == n:
            return False
    
    x0 = 3*(x//3)
    y0 = 3*(y//3)
    
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j]==n:
                return False
    
    return True

################################################

def sudoku():
    global backtracking
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y]==0:
                for n in range(1,10):
                    if is_valid(x, y, n):
                        grid[x][y]= n
                        sudoku()
                        grid[x][y]= 0
                        backtracking=backtracking+1
                return grid
    
    print(np.matrix(grid))
    
#############################################

sudoku()
print(backtracking)
                    
            
        


