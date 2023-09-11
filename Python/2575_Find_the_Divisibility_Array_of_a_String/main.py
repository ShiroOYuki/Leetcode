class Solution:
    def divisibilityArray(self, word: str, m: int) -> list:
        ans = []
        pre = 0
        for c in word:
            pre = (pre * 10 + int(c)) % m
            ans.append(1 if pre == 0 else 0)
        return ans
    
# 7 % 4 = 3
# 72 % 4 = (30 + 2) % 4 = 0
    
s = Solution()
print(s.divisibilityArray(word = "1010", m = 10))
                
        
        