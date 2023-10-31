class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        res = [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]
        return res
    
print(Solution().findArray(pref = [5,2,0,3,1]))
        
        
        