class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        res = 0
        n = len(colors)
        flag = 0
        for i in range(n-1):
            if colors[i+1] != colors[i]:
                if colors[i] == "A":
                    res += max(i-flag-1, 0)
                    flag = 0
                else:
                    res -= max(i-flag-1, 0)
                    flag = 0
                flag = i+1
        return res > 0

print(Solution().winnerOfGame("AABBBA"))
        
    