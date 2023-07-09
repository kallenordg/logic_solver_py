GRID_SIZE = 8

def can_place(grid, row, col, num):
    for i in range(GRID_SIZE):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_grid(grid, row, col):
    if row == GRID_SIZE:
        return True
    if col == GRID_SIZE:
        return solve_grid(grid, row + 1, 0)
    if grid[row][col] != 0:
        return solve_grid(grid, row, col + 1)
    for i in range(1, GRID_SIZE + 1):
        if can_place(grid, row, col, i):
            grid[row][col] = i
            if solve_grid(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False

def solvable_grid(grid, row, col):
    if row == GRID_SIZE:
        return grid
    if col == GRID_SIZE:
        return solvable_grid(grid, row + 1, 0)
    if grid[row][col] != 0:
        return solvable_grid(grid, row, col + 1)
    for i in range(1, GRID_SIZE + 1):
        if can_place(grid, row, col, i):
            grid[row][col] = i
            if solve_grid(grid, row, col + 1):
                return grid
            grid[row][col] = 0
    return grid

def solution(grid):
    if solve_grid(grid,0,0):
        return(solvable_grid(grid, 0, 0))
    else:
        return("Unsolvable") 

grid = [
    [0,0,-1,8,6,0,0,4],
    [0,-1,0,7,5,1,4,3],
    [5,2,7,0,-1,0,0,8],
    [6,0,0,0,8,5,-1,1],
    [0,5,8,0,4,0,3,-1],
    [4,0,0,-1,0,7,6,0],
    [-1,0,0,0,1,6,5,2],
    [8,1,4,2,0,-1,0,0]
]

solved_grid = [
    [1,7,-1,8,6,3,2,4],
    [2,-1,6,7,5,1,4,3],
    [5,2,7,6,-1,4,1,8],
    [6,4,2,3,8,5,-1,1],
    [7,5,8,1,4,2,3,-1],
    [4,3,1,-1,2,7,6,5],
    [-1,8,3,4,1,6,5,2],
    [8,1,4,2,3,-1,7,6]
]

print(solution(grid) == solved_grid)
