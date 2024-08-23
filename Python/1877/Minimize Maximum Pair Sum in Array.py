class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums = sorted(nums)
        maxPair = 0
        for i in range(len(nums)//2):
            if nums[i] + nums[-i-1] > maxPair:
                maxPair = nums[i] + nums[-i-1]
        return maxPair

print(Solution().minPairSum([3, 5, 2, 3]))