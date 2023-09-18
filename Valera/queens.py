# N-Queens Problem Solver
# This program aims to solve the 8-Queens problem

# Leobardo Valera
# Sep 01 2023

import numpy as np

n = 8

grid = [[0 for i in range(n)] for j in range(n)]

backtracking = 0


##############################################
def is_valid(x,y):
    

    # Left top point of the main diagonal
    top_left_x = x-min(x,y)
    top_left_y = y-min(x,y)
    
    # Botton right point of the main diagona;
    botton_right_x = x+ min(n-1-x, n-1-y)
    botton_right_y = y+ min(n-1-x, n-1-y)
    
    # Botton left point of the secondary diagonal
    botton_left_x = x-min(x,n-1-y)
    botton_left_y = y+min(x,n-1-y)
    
    # Top right point of the secondary diagonal
    top_right_x = x+min(n-1-x,y)
    top_right_y = y-min(n-1-x,y)
    
    
    length_main_diagonal = min(botton_right_x-top_left_x,botton_right_y-top_left_y)
    length_sec_diagonal =min(top_right_x-botton_left_x,botton_left_y-top_right_y)
    
    for i in range(n):
        if grid[i][y]!=0:
            return False
    
    for j in range(n):
        if grid[x][j]!=0:
            return False
        
    for i in range(length_main_diagonal):
        if grid[top_left_x+i][top_left_y+i]!=0:
            return False
    
    for i in range(length_sec_diagonal):
        if grid[botton_left_x+i][botton_left_y-i]!=0:
            return False
    
    return True
    
    
        
################################################
backtracking = 0
q = 0

def solve_queen():
    global grid
    global q
    global backtracking
    
    if q==n:
        return True
    
    for row in range(n):
        
        if is_valid(row,q): 
            grid[row][q]=1
            q = q+1 
            if solve_queen():
                return True
            q=q-1
            grid[row][q]=0
            backtracking = backtracking + 1
    return False
        
            
    
#############################################

# Testing the function

solve_queen()
print(np.matrix(grid))
print(backtracking)
                    
            
        


