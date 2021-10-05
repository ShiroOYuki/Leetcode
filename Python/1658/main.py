class Solution:
    def minOperations(self, nums: list, x: int):
        i = j = 0
        while x > sum(num[i:j]):


s = Solution()
print(s.minOperations(nums=[1, 1, 4, 2, 3], x=5))
