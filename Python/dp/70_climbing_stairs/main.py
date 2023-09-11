class Solution:
    def __init__(self):
        self.t = {}
    
    def climbStairs(self, n: int) -> int:
        if not self.t.get(n):
            if n <= 1:
                return 1
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.t[n] = result
            return result
        return self.t[n]

s = Solution()
print(s.climbStairs(30))
print(s.t)