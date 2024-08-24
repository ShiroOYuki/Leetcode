# https://leetcode.com/problems/maximum-number-of-points-with-cost/description/

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        score = [0]*len(points[0])
        prev_idx = None
        
        for k in range(len(points[0])):
            score[k] = points[0][k]
            prev_idx = k
            for i in range(1, len(points)):
                calc_idx = None
                prev_score = None
                for j in range(len(points[i])):
                    calc_score = 0
                    
                    if prev_idx is not None:
                        calc_score = points[i][j] - abs(prev_idx - j)
                    else:
                        calc_score = points[i][j]
                        
                    if prev_score is None or prev_score < calc_score:
                        calc_idx = j
                        prev_score = calc_score
                        
                prev_idx = calc_idx
                score[k] += prev_score
    
s = Solution()
print(s.maxPoints([[0,0,4,1,4],[2,1,2,0,1],[2,2,1,3,4],[5,2,4,5,4],[0,5,4,2,5]]))