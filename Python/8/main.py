class Solution:
    def myAtoi(self, s: str):
        f = False
        s = s.replace(" ", "")
        s = s.split(".")
        s = s[0]
        if s == "" or ("-" in s and "+" in s) or s == "+" or s == "-":
            return 0
        s2 = ""
        for c in s:
            if c in "+-1234567890":
                f = True
                s2 += c
            elif c != " " and f == False or c not in "+-1234567890":
                return 0
        min = pow(2, 31)*-1
        _max = pow(2, 31)-1
        ans = int(s2)
        if ans > _max:
            ans = _max
        if ans < min:
            ans = min
        return ans


s = Solution()
ans = s.myAtoi("+-12")
print(ans, type(ans))
