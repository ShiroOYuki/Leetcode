# 路徑規劃，但權重為節點間的差
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        stack = [(0, 0)]
        rows = len(heights)
        cols = len(heights[0])
        seen = list(list(False for _ in range(cols)) for __ in range(rows))
        dist = list(list(float("-inf") for _ in range(cols)) for __ in range(rows))
        while stack:
            (i, j) = stack.pop(0)
            if not seen[i][j]:
                if i > 0:
                    dist[i][j] = max(dist[i-1][j], abs(heights[i-1][j] - heights[i][j]))
                    stack.append((i-1, j))
                if i+1 < rows:
                    dist[i][j] = max(dist[i+1][j], abs(heights[i+1][j] - heights[i][j]))
                    stack.append((i+1, j))
                if j > 0:
                    dist[i][j] = max(dist[i][j-1], abs(heights[i][j-1] - heights[i][j]))
                    stack.append((i, j-1))
                if j+1 < cols:
                    dist[i][j] = max(dist[i][j+1], abs(heights[i][j+1] - heights[i][j]))
                    stack.append((i, j+1))
                seen[i][j] = True
    
            for k in dist:
                for q in k:
                    print(q, end="\t")
                print()
        
Solution().minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])