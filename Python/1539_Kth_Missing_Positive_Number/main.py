class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:
        n = len(arr) - 1
        num = 0
        idx = 0
        while k > 0:
            num += 1
            if num == arr[idx]:
                if idx < n:
                    idx += 1
                continue
            k -= 1
        return num
    
s = Solution()
print(s.findKthPositive(arr = [1, 2, 5, 6, 10], k = 3))