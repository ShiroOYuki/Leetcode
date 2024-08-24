class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """
        - 創建 2D Array (max_ary)，用於儲存每個點計算出來的最大值
        - max_ary[0] = points[0] (因為沒有前一排，所以計算出的最大值直接是當前的點)
        
        for i in range(len(points[1:])):
            1. 由左到右找出前一行的最大值
            2. 由右到左找出前一行的最大值
            3. 計算 prev_idx = curr_idx 時的值
            4. 將以上三個值取最大值，並存入 max_ary
        """
        m = len(points)
        n = len(points[0])
        
        prev_max = points[0]
        for i in range(1, m-1):
            left_max = [0]*n
            right_max = [0]*n
            curr_max = [0]*n
            
            # 由左到右計算最大值
            for j in range(1, n):
                left_max[j] = max(prev_max[j-1]-1, prev_max[j])
                
            # 由右到左計算最大值
            for j in range(n-2, -1, -1):
                right_max[j] = max(prev_max[j+1]-1, prev_max[j])
            
            for j in range(n):
                curr_max[j] = points[i][j] + max(left_max, right_max)
                
            prev_max = curr_max
                
        return max(prev_max)    
    
s = Solution()
print(s.maxPoints([[0,0,4,1,4],[2,1,2,0,1],[2,2,1,3,4],[5,2,4,5,4],[0,5,4,2,5]]))