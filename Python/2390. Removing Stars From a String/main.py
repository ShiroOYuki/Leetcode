class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        n = len(s)
        while i < n:
            # print(s, n)
            # print(" "*i + ".")
            if s[i] == "*":
                if i > 1:
                    s = s[:i-1] + s[i+1:]
                    i -= 1
                    n -= 2
                else:
                    s = s[i+1:]
                    n -= (i+1)
                    i = 0
            else:
                i += 1
        return s
                
s = Solution()
print(s.removeStars("**l*eet**cod*e"))
                