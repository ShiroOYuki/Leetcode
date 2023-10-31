class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        res = [pref[0]]*n
        for i in range(1, n):
            res[i] = pref[i] ^ pref[i-1]
        return res
    
print(Solution().findArray(pref = [5,2,0,3,1]))
        
        
        