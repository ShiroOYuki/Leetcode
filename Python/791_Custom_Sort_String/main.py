from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        wordList = defaultdict(lambda: -1)
        n = 0
        for w in order:
            if wordList[w] == -1:
                wordList[w] = n
                n += 1
                
        s = list(s)
        for i in range(len(s)):
            for j in range(i):
                if wordList[s[i]] < wordList[s[j]]:
                    s[i], s[j] = s[j], s[i]
        
        return "".join(s)
        
        
print(Solution().customSortString("bca", "acbac"))