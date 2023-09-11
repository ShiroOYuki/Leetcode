#TLE

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums
        res = []
        m = float("-inf")
        nk = 0-k
        for i in range(len(nums)-k+1):
            if nk < i:
                m = float("-inf")
            if i - nk >= k or m == float("-inf"):
                for j in range(k):
                    if nums[i+j] > m:
                        m = nums[i+j]
                        nk = i+j
            if nums[i+k-1] > m:
                m = nums[i+k-1]
                nk = i+k-1
            res.append(m)
        return res
    
print(Solution().maxSlidingWindow(nums = [7,2,4], k = 2))
            