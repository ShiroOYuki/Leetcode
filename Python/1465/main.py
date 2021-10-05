class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list):
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        mh = 0
        mv = 0
        for i in range(1, len(horizontalCuts)):
            if horizontalCuts[i]-horizontalCuts[i-1] > mh:
                mh = horizontalCuts[i]-horizontalCuts[i-1]
        for i in range(1, len(verticalCuts)):
            if verticalCuts[i]-verticalCuts[i-1] > mv:
                mv = verticalCuts[i]-verticalCuts[i-1]
        return (mv*mh) % (int(1e9)+7)  # return 10^9+7


s = Solution()
print(s.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
