import matplotlib.pyplot as plt
import random

ccgrid_size = (9, 9)
grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]

def showGrid(grid):
    plt.imshow(grid, cmap="binary")
    plt.pause(0.5)
    plt.clf()
def getNeighbours(x, y, grid):
    return (
        grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1] +
        grid[y][x-1]               +  grid[y][x+1] +
        grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1]
    )
def updateGrid(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            neighbours = getNeighbours(x, y, grid)

            if grid[y][x] == 1 and neighbours in [2, 3]:
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and neighbours == 3:
                new_grid[y][x] = 1
    return new_grid
def randomSeed(grid, density=0.3):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = 1 if random.random() < density else 0

randomSeed(grid, 0.3)

plt.figure()
for step in range(50):  
    showGrid(grid)
    new_grid = updateGrid(grid)
    
    if new_grid == grid:
        print(f"Simulation stopped at step {step} (stable grid).")
        break
    
    grid = new_grid

plt.show()

