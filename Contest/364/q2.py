class Solution:
    def maximumSumOfHeights(self, maxHeights: list[int]) -> int:
        n = len(maxHeights)
        
                
        m = max(maxHeights)
        # mids = [i for i in range(n) if maxHeights[i] == m]
        maxHeights_copy = maxHeights.copy()
        
        res = 0
        last = None
        for mid in range(n):
            maxHeights = maxHeights_copy.copy()
            if not last or maxHeights[mid] != last:
                last = maxHeights[mid]
                for i in range(mid, 0, -1):
                    if maxHeights[i-1] > maxHeights[i]:
                        maxHeights[i-1] = maxHeights[i]
                for i in range(mid+1, n):
                    if maxHeights[i-1] < maxHeights[i]:
                        maxHeights[i] = maxHeights[i-1]
            res = max(res, sum(maxHeights))
            
        return res
            
                    
print(Solution().maximumSumOfHeights([5,2,4,2,4]))