class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        W = len(obstacleGrid[0])
        H = len(obstacleGrid)
        m = []
        for i in range(H):
            m.append([0]*W)
        m[0][0] = 1
            
        for i in range(H):
            for j in range(W):
                if obstacleGrid[i][j] == 0:
                    if i > 0:
                        m[i][j] += m[i-1][j]
                    if j > 0:
                        m[i][j] += m[i][j-1]
        return m[-1][-1] * (1-obstacleGrid[0][0])

print(Solution().uniquePathsWithObstacles(
    [[1]]
))