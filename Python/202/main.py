class Solution:
    def isHappy(self, n: int):
        return self.dp(n, []) == 1

    def dp(self, n, l: list):
        if n in l:
            return -1
        l.append(n)
        if n == 1:
            return n
        else:
            i = 1
            num = 0
            while i <= n*10:
                j = (n % i)//(i/10)
                num += j**2
                n -= j*(i/10)
                i *= 10
            return self.dp(num, l)


s = Solution()
print(s.isHappy(n=2))
