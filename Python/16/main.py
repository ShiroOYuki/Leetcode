# use "Two Pointer"

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        print(nums)
        a = nums[0]
        b = nums[1]
        c = nums[-1]
        ans = a+b+c
        print(ans)
        for i in range(len(nums)-2):
            a = nums[i]
            bindex = i+1
            cindex = -1
            for j in range(i+1, len(nums)-1):
                b = nums[bindex]
                c = nums[cindex]
                if abs(a+b+c-target) < abs(ans-target):
                    print(a, b, c)
                    ans = a+b+c
                if a+b+c == target:
                    return a+b+c
                if a+b+c > target:
                    cindex -= 1
                elif a+b+c < target:
                    bindex += 1
                print(ans, a, b, c)
        return ans


s = Solution()
print(s.threeSumClosest([-111, -111, 3, 6, 7, 16, 17, 18, 19], 13))

"""
[1,2,3,4,5,6]
i = 1
2~3

"""
