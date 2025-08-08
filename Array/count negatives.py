def countNegatives(grid):
    count=0
    # Implement your solution here
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]<0:
                count+=1
    return count
