class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        right = max(piles)
        if len(piles) == 1:
            k = right // h
            if right % h != 0:
                k += 1
            return k
        left = 0
        while left < right:
            k = max(1, (right + left) // 2)
            c = 0
            for i in piles:
                c += i // k
                if i % k != 0:
                    c += 1
            if c <= h:
                right = k
            else:
                left = k+1
        return k + 1 if c > h else k
    
s = Solution()
print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6))