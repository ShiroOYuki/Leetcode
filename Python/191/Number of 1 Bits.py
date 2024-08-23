class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while 2**i < n:
            i += 1
        c = 0
        while n > 0:
            print(n)
            if n >= 2**i:
                n -= 2**i
                c += 1
            i -= 1
        return c
    
print(Solution().hammingWeight(128))