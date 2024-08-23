class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        return sum([sorted(piles)[int(len(piles)/3) + i] for i in range(0, int(len(piles)/3*2), 2)])

print(Solution().maxCoins([6,4,5,2,1,3]))