# Knight Tour
# Created by Leobardo Valera

import numpy as np

n = 8 

board = [[0  for  j in range(n)] for i in range(n)]

steps = [[2, 1], [1, 2],[-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2],[2, -1]]
#steps = [[-1, -2], [1, -2],[-2, -1], [2, -1], [2, 1], [1, 2], [-1, 2],[-2, 1]]

##############################################################

def safe_to_jump(x,y):
    global board
    if (x<0) or (x>n-1) or (y<0) or (y>n-1) or (board[x][y]!=0):
        return False
    return True

#############################################################

def knight(board,x,y,p):
    global backtracking
    if p == 64:
        return True

    for i in range(8):
        next_x = x+steps[i][0]
        next_y = y+steps[i][1]
        
        if safe_to_jump(next_x,next_y):
            board[next_x][next_y] = p+1
            if knight(board,next_x,next_y,p+1):
                return True
            bactracking = backtracking + 1
            board[next_x][next_y] = 0
        
    return False

#########################################################
backtracking = 0  
p=1
board[0][0] = 1
knight(board,0,0,p)


print(np.matrix(board))
print(backtracking)
          
            
        