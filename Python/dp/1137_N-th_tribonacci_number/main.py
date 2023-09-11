class Solution:
    def __init__(self):
        self.t = {}
    
    def tribonacci(self, n: int) -> int:
        if n > 1:
            if not self.t.get(n):
                self.t[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return self.t[n]
        elif n<0:
            return 0
        return n

for i in range(8):
    print(Solution().tribonacci(i))
print(Solution().tribonacci(25))