class Solution:
    def jump(self, nums: list):
        if len(nums) <= 1:
            return 0
        if len(nums) <= 2:
            return 1
        ind = 0
        c = 1
        nind = 0
        m = nums[ind]
        lm = 0
        while ind+m < len(nums)-1:
            for i in range(ind+1, ind+m+1):
                if nums[i] >= lm:
                    lm = nums[i]
                    nind = i
            m = lm
            ind = nind
            lm = 0
            c += 1
            print(m, ind)
        return c


s = Solution()
print(s.jump([1, 2, 3]))
print()
print(s.jump([2, 3, 0, 1, 4]))
print()
print(s.jump([1, 3, 2]))
print()
print(s.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
