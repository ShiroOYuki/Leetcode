class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles = sorted(piles)
        piles = piles[int(len(piles)/3):]
        return sum([piles[i] for i in range(0, len(piles), 2)])

print(Solution().maxCoins([6,4,5,2,1,3]))