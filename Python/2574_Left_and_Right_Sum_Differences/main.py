class Solution:
    def leftRigthDifference(self, nums: list) -> list:
        size = len(nums)
        leftSum = [0] * size
        rightSum = [0] * size
        for i in range(1, size):
            leftSum[i] += leftSum[i-1] + nums[i-1]
            rightSum[size - 1 - i] += rightSum[size - i] + nums[size - i]
        return [abs(i - j) for (i, j) in zip(leftSum, rightSum)]
        
s = Solution()
print(s.leftRigthDifference([10]))
