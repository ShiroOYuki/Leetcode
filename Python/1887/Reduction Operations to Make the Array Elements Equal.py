class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums = sorted(nums)
        indexStamp = [0]*len(nums)
        now = nums[0]
        for i, n in enumerate(nums):
            indexStamp[i] = indexStamp[i-1]
            if n != now:
                indexStamp[i] += 1
                now = n
        return sum(indexStamp)
    
print(Solution().reductionOperations([1,1,2,2,3]))
                