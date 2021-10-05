class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle not in haystack:
            return -1
        if needle == haystack:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i


s = Solution()
print(s.strStr("abc", "c"))
