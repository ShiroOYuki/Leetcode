class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for i in range(len(s)):
            while True:
                if index == len(t):
                    return False
                if s[i] == t[index]:
                    index += 1
                    break
                index += 1
        return True
            
s = Solution()
print(s.isSubsequence("bdc", "ahbgdc"))