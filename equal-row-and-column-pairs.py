#2352 equal-row-and-column-pairs
grid = [[3,2,1],[1,7,6],[2,7,7]]
def equal_pairs(grid):
    count=0
    n=len(grid)
    freq={}
    for row in grid:
        key=tuple(row)
        freq[key]=freq.get(key,0)+1
    for j in range(n):
        col=tuple(grid[i][j] for i in range(n))
        count+=freq.get(col,0)
    return count
print(equal_pairs(grid))