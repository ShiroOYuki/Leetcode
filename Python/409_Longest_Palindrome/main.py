class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        seq = defaultdict(int)
        length = 0
        for i in s:
            seq[i] += 1
            if seq[i] == 2:
                length += 2
                del seq[i]
        if seq:
            length += 1
        return length
        
        
s = Solution()
print(s.longestPalindrome("abccccdd"))