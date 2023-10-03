class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        monotonic = 0
        for i in range(len(nums) - 1):
            if monotonic == 0:
                if nums[i] < nums[i+1]:
                    monotonic = 1
                elif nums[i] > nums[i+1]:
                    monotonic = -1
            else:
                if monotonic == -1 and nums[i] >= nums[i+1]:
                    continue
                elif monotonic == 1 and nums[i] <= nums[i+1]:
                    continue
                else:
                    return False
        return True

print(Solution().isMonotonic([4,3,1, -1]))