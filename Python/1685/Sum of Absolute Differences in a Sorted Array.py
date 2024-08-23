class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0]*n
        for i in range(n):
            for j in range(i, n):
                res[i] += nums[j] - nums[i]
                res[j] += nums[j] - nums[i]
        return res
    
print(Solution().getSumAbsoluteDifferences([1,4,6,8,10]))