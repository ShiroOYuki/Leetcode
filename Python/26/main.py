class Solution:
    def removeDuplicates(self, nums: list):
        if nums == []:
            return 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == nums[i+1]:
                nums.pop(i)
        return len(nums)


s = Solution()

print(s.removeDuplicates([1, 1, 2]))
