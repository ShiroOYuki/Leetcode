class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=1 or s==s[::-1]:
            return s
        ans = s[0]
        for i in range(len(s)):
            count = 0
            while True:
                str1 = s[i-count:i+count+1]
                if str1 == str1[::-1] and i >= count and len(str1):
                    if len(str1) > len(ans):
                        ans = s[i-count:i+count+1]
                    count += 1
                else:
                    break
            count = 0
            while True:
                str1 = s[i-count:i+count+2]
                if str1 == str1[::-1] and i >= count and len(str1):
                    if len(str1) > len(ans):
                        ans = s[i-count:i+count+2]
                    count += 1
                else:
                    break
        return ans


s = Solution()
print(s.longestPalindrome("babab"))
