"""
1605. Find Valid Matrix Given Row and Column Sums

- Question:
You are given two arrays rowSum and colSum of non-negative integers where 
rowSum[i] is the sum of the elements in the ith row and colSum[j] is the 
sum of the elements of the jth column of a 2D matrix. In other words, you 
do not know the elements of the matrix, but you do know the sums of each 
row and column.

Find any matrix of non-negative integers of size rowSum.
length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. 
It's guaranteed that at least one matrix that fulfills the requirements exists.

---

- Hint:
Find the smallest rowSum or colSum, and let it be x. 
Place that number in the grid, and subtract x from rowSum and colSum. 
Continue until all the sums are satisfied.

---

- Example:
Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
"""

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0]*n for _ in range(m)]
        
        def min_g_zero(x):
            res = max(x)
            idx = 0
            for iidx, i in enumerate(x):
                if 0 < i <= res: 
                    res = i
                    idx = iidx
            return res, idx
        
        while True:
            xr, xri = min_g_zero(rowSum)
            xc, xci = min_g_zero(colSum)
            if xc <= 0 or xr < xc: x = xr
            if xr <= 0 or xc <= xr: x = xc
            if sum(rowSum) + sum(colSum) == 0: break
            
            matrix[xri][xci] += x
            x = matrix[xri][xci]
            
            rowSum[xri] -= x
            colSum[xci] -= x
            
        return matrix

s = Solution()
print(s.restoreMatrix(rowSum = [14, 9], colSum = [6, 9, 8]))