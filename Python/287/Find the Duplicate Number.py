class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        seen = list(False for _ in range(n))
        for i in nums:
            if seen[i]:
                return i
            seen[i] = True
        return -1

print(Solution().findDuplicate([1, 4, 2, 3, 4]))