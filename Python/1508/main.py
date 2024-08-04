class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sum_arr = [0]*sum(range(1, n+1))
        idx = 0
        for i in range(n):
            for j in range(i, n):
                sum_arr[idx] = sum(nums[i:j+1])
                idx += 1
        return sum(sorted(sum_arr)[left-1:right]) % (10**9 + 7)
        
s = Solution()
print(s.rangeSum([1, 2, 3, 4], 4, 1, 5))