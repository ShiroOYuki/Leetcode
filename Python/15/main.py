# use "Two Pointer"

class Solution:
    def threeSum(self, nums: list):
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            bindex = i+1
            cindex = -1
            for j in range(i+1, len(nums)-1):
                b = nums[bindex]
                c = nums[cindex]
                if a+b+c > 0:
                    cindex -= 1
                elif a+b+c < 0:
                    bindex += 1
                else:
                    if [a, b, c] not in ans:
                        ans.append([a, b, c])
                    bindex += 1
        return ans


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

"""
[1,2,3,4,5,6]
i = 1
2~3

"""
