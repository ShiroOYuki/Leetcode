class Solution:
    def maxArea(self, height: list):
        if len(height) <= 1:
            return 0
        if len(height) == 2:
            return min(height)
        l = 0
        r = len(height)-1
        ans = 0
        while not r == l:
            if min(height[l], height[r])*(r-l) > ans:
                ans = min(height[l], height[r])*(r-l)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans


s = Solution()
print(s.maxArea([4, 3, 2, 1, 4]))
