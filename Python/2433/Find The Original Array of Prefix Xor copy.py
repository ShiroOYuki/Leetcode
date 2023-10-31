class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]
    
print(Solution().findArray(pref = [5,2,0,3,1]))
        
        
        