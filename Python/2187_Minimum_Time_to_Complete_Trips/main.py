class Solution:
    def minimumTime(self, time: list, totalTrips: int) -> int:
        left = 0
        right = min(time) * totalTrips
        while right > left:
            step = (left + right) // 2
            print(step, left, right)
            if sum(step // t for t in time) >= totalTrips:
                right = step
            else:
                left = step + 1
        return left
                
s = Solution()
print(s.minimumTime([1, 2, 3], 9))