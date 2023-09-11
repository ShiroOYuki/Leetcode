class Solution:
    def pivotIndex(self, nums) -> int:
        length = len(nums)
        left, right = 0, 0
        for i in range(1, length):
            right += nums[i]
        for i in range(length):
            if left == right:
                return i
            if i+1 >= length:
                break
            left += nums[i]
            right -= nums[i+1]
        return -1
    
s = Solution()
print(s.pivotIndex([-1, -1, 1, 1, 1, 1]))