import matplotlib.pyplot as plt
import random

# ---------- Base Grid Setup ----------
grid_size = (9, 9)  # a 9x9 grid (rows, columns)
grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]  # start with all 0s

# ---------- Visualization ----------
def showGrid(grid):
    plt.imshow(grid, cmap="binary")  # display grid in black & white
    plt.pause(0.5)  # wait 0.5 seconds so animation is visible
    plt.clf()       # clear the old frame before drawing the next

# ---------- Helper Functions ----------
def getNeighbours(x, y, grid):
    # Add up all 8 surrounding cells
    return (
        grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1] +
        grid[y][x-1]               +  grid[y][x+1] +
        grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1]
    )

def updateGrid(grid):
    # Create a new empty grid (all zeros)
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    # Loop through cells (skip borders to avoid errors)
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            neighbours = getNeighbours(x, y, grid)

            # Apply Conway’s Game of Life rules
            if grid[y][x] == 1 and neighbours in [2, 3]:
                new_grid[y][x] = 1  # cell survives
            elif grid[y][x] == 0 and neighbours == 3:
                new_grid[y][x] = 1  # cell is born
            # else cell stays 0 (dies or stays dead)
    return new_grid

def randomSeed(grid, density=0.3):
    # Fill grid with 1 (alive) randomly based on density %
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = 1 if random.random() < density else 0

# ---------- Run Simulation ----------
randomSeed(grid, 0.3)  # start with 30% alive cells

plt.figure()
for step in range(50):  # run for up to 50 generations
    showGrid(grid)
    new_grid = updateGrid(grid)
    
    if new_grid == grid:  # stop if nothing changes
        print(f"Simulation stopped at step {step} (stable grid).")
        break
    
    grid = new_grid  # update grid for next generation

plt.show()

