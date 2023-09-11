class Solution:
    def fib(self, n: int) -> int:
        return self.fib(n-1) + self.fib(n-2) if n>1 else n

for i in range(8):
    print(Solution().fib(i))