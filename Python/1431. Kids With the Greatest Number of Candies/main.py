class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = 0
        for i in candies:
            if i > m:
                m = i
        for idx in range(len(candies)):
            if candies[idx] + extraCandies < m:
                candies[idx] = False
            else:
                candies[idx] = True
        return candies