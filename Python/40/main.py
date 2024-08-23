class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if target <= 0: return None
        candidates.sort()
        print(candidates, target)
        res = [[candidates[0]]]
        
        for i in range(len(candidates)-2):
            for j in range(i, len(candidates)-1):
                rres = self.combinationSum2(candidates[j+1:], target-candidates[j])
                if rres is not None:
                    rres = [[candidates[i]] + k for k in rres]
                    res += rres
            
        return res

s = Solution()
print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))