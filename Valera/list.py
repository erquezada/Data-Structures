import numpy as np
# Lists
List = [1,2,3, 'Hello', 4]
print(List)
print(List[3])

grid = [
        [5,3,0,0,7,0,0,0,0], 
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
        ]
print(np.matrix(grid))

grid[0][2] = 3
print(np.matrix(grid[0][2]))
print()
print(np.matrix(grid))

for i in range(9):
    print(i)

print()

for i in range(9):
    if (i == 5):
        print(i)

def function():
    print("Hello World")

    return 0


# create function take a number n from a value from 1 to 9
# number cannot be repeated in any column or square

def is_valid(x,y,n):
    global grid
    for i in range(9):
        if (grid[x][i] == n):
            return False
    
    for i in range(9):
        if (grid[i][y] == n):
            return False
    
    return True
            
print(is_valid(0,5,8))

# check square

def is_valid_neighbor(x,y,n):
    global grid
    for i in range(3):
        for j in range(3):
           if (grid[x+i][y+j] == n):
               return False
           
    return True

print(is_valid_neighbor(0,4,8))
print(np.matrix(grid))