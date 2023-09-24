class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = s.count("1")
        n = len(s)
        if c >= 1:
            return "1"*(c-1) + "0"*(n-c) + "1"
        else:
            return s
        
print(Solution().maximumOddBinaryNumber("000"))
            