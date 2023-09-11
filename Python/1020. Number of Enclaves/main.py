class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = []
        for i in range(m):
            visited.append([0]*n)
        q = []
        
        # Step 1. 過濾連在邊界的地塊
        for j in range(n):
            # top
            if grid[0][j] == 1:
                q.append((0, j))
            # bottom
            if grid[m-1][j] == 1:
                q.append((m-1, j))
        
        for j in range(m):
            # left
            if grid[j][0] == 1:
                q.append((j, 0))
            # right
            if grid[j][n-1] == 1:
                q.append((j, n-1))
        
        while q:
            i, j = q.pop(0)
            if visited[i][j] != 1:
                if i-1 > 0 and grid[i-1][j] == 1:
                    q.append((i-1, j))
                if i+1 < m and grid[i+1][j] == 1:
                    q.append((i+1, j))
                if j-1 > 0 and grid[i][j-1] == 1:
                    q.append((i, j-1))
                if j+1 < n and grid[i][j+1] == 1:
                    q.append((i, j+1))
                visited[i][j] = 1      
        
        # Step 2. 找沒有連接邊界的地塊
        res = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 1 and visited[i][j] != 1:
                    res += 1
        return res
    
s = Solution()
print(s.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]))