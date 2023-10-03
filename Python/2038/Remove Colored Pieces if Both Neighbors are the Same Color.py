class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        aTags = [-1]*n
        bTags = [-1]*n
        res = 0
        for i in range(n-1):
            if colors[i+1] == colors[i] == "A":
                aTags[i] += 1
                aTags[i+1] += 1
            elif colors[i+1] == colors[i] == "B":
                bTags[i] += 1
                bTags[i+1] += 1
            if aTags[i] > 0:
                res += 1
            if bTags[i] > 0:
                res -= 1
        return res > 0

print(Solution().winnerOfGame("AABBBA"))
        
    