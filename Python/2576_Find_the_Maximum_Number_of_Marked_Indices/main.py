# Failed

class Solution:
    def maxNumOfMarkedIndices(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0
        t = sorted(nums)
        nums = t[::-1]
        result = 0
        while True:
            print(nums)
            f = False
            for i in range(1, len(nums)):
                if nums[i] * 2 < nums[0]:
                    result += 2
                    nums.pop(i)
                    nums.pop(0)
                    f = True
                    break
            if not f:
                ans = result
                nums = t
                result = 0
                break
        while True:
            print(nums)
            f = False
            for i in range(1, len(nums)):
                if nums[0] * 2 < nums[i]:
                    result += 2
                    nums.pop(i)
                    nums.pop(0)
                    f = True
                    break
            if not f:
                print(result, ans)
                return max(result, ans) 
            

s = Solution()
print(s.maxNumOfMarkedIndices([42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]))