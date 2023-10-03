class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            if i % 2 == 1:
                res.append(i)
            else:
                res.insert(0, i)
        return res
    
print(Solution().sortArrayByParity([4,3,2,1]))