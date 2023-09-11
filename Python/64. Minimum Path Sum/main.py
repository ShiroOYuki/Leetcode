import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def minPathSum(self, grid: list) -> int:
        row_length = len(grid)
        col_length = len(grid[0])
        row, col = 0, 0
        m = []
        for _ in range(row_length):
            m.append([float("inf")]*col_length)
        m[0][0] = grid[0][0]
        q = [[0, 0]]
        while q:
            row, col = q.pop(0)
            now = m[row][col]
            # if col > 0:
            #     if now + grid[row][col-1] < m[row][col-1]:
            #         m[row][col-1] = now + grid[row][col-1]
            #         q.append([row, col-1])
            if col < col_length-1:
                if now + grid[row][col+1] < m[row][col+1]:
                    m[row][col+1] = now + grid[row][col+1]
                    q.append([row, col+1])
            # if row > 0:
            #     if now + grid[row-1][col] < m[row-1][col]:
            #         m[row-1][col] = now + grid[row-1][col]
            #         q.append([row-1, col])
            if row < row_length-1:
                if now + grid[row+1][col] < m[row+1][col]:
                    m[row+1][col] = now + grid[row+1][col]
                    q.append([row+1, col])
        res = m[-1][-1]
        print(m)
        def draw(m, grid):
            img = []
            row_length = len(m)
            col_length = len(m[0])
            col, row = 0, 0
            m[0][0] = 0
            grid[0][0] = 0
            while [row, col] != [row_length-1, col_length-1]:
                if row+1 == row_length:
                    col += 1
                elif col+1 == col_length:
                    row += 1
                elif m[row+1][col] < m[row][col+1]:
                    row += 1
                else:
                    col += 1
                m[row][col] = 0
                grid[row][col] = 0
            grid = np.array(grid)
            m = np.array(m)
            print(np.max(m))
            img = (np.zeros((row_length, col_length)) + 255 - (grid / np.max(grid)*255)).astype(np.float32)
            plt.imshow(img, cmap="hot")
            plt.show()
            img = (np.zeros((row_length, col_length)) + 255 - (m / np.max(m) * 255)).astype(np.float32)
            plt.imshow(img, cmap="cool")
            plt.show()
            
        draw(m, grid)
        return res
    

s = Solution()
grid = np.random.randint(0, 100, (1000, 1000))
print(s.minPathSum(grid = [[5,4,2,9,6,0,3,5,1,4,9,8,4,9,7,5,1],[3,4,9,2,9,9,0,9,7,9,4,7,8,4,4,5,8],[6,1,8,9,8,0,3,7,0,9,8,7,4,9,2,0,1],[4,0,0,5,1,7,4,7,6,4,1,0,1,0,6,2,8],[7,2,0,2,9,3,4,7,0,8,9,5,9,0,1,1,0],[8,2,9,4,9,7,9,3,7,0,3,6,5,3,5,9,6],[8,9,9,2,6,1,2,5,8,3,7,0,4,9,8,8,8],[5,8,5,4,1,5,6,6,3,3,1,8,3,9,6,4,8],[0,2,2,3,0,2,6,7,2,3,7,3,1,5,8,1,3],[4,4,0,2,0,3,8,4,1,3,3,0,7,4,2,9,8],[5,9,0,4,7,5,7,6,0,8,3,0,0,6,6,6,8],[0,7,1,8,3,5,1,8,7,0,2,9,2,2,7,1,5],[1,0,0,0,6,2,0,0,2,2,8,0,9,7,0,8,0],[1,1,7,2,9,6,5,4,8,7,8,5,0,3,8,1,5],[8,9,7,8,1,1,3,0,1,2,9,4,0,1,5,3,1],[9,2,7,4,8,7,3,9,2,4,2,2,7,8,2,6,7],[3,8,1,6,0,4,8,9,8,0,2,5,3,5,5,7,5],[1,8,2,5,7,7,1,9,9,8,9,2,4,9,5,4,0],[3,4,4,1,5,3,3,8,8,6,3,5,3,8,7,1,3]]))
print(s.minPathSum(grid=grid))
                
                