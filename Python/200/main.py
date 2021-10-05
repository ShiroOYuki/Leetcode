class Solution:
    def numIslands(self, grid: list):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        grid[i][j] = "0"
        if i-1 >= 0 and grid[i-1][j] == "1":
            self.dfs(grid, i-1, j)
        if i+1 < len(grid) and grid[i+1][j] == "1":
            self.dfs(grid, i+1, j)
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.dfs(grid, i, j-1)
        if j+1 < len(grid[i]) and grid[i][j+1] == "1":
            self.dfs(grid, i, j+1)


s = Solution()
print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
