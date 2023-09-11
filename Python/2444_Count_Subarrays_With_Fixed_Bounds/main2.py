class Solution:
    def countSubarrays(self, nums: int, minK: int, maxK: int) -> int:
        length = len(nums)
        lastMaxIndex = -1
        lastMinIndex = -1
        startIndex = 0
        result = 0
        for i in range(length):
            # 不符合範圍: 重置
            if nums[i] < minK or nums[i] > maxK:
                lastMaxIndex = -1
                lastMinIndex = -1
                startIndex = i + 1
                
            # 找到最小值: 紀錄
            if nums[i] == minK:
                lastMinIndex = i
                
            # 找到最大值: 紀錄
            if nums[i] == maxK:
                lastMaxIndex = i
            
            # 找到 min, max 後，只要下次找到的數字有在範圍內就把 result + 1
            if lastMinIndex >= 0 and lastMaxIndex >= 0:
                t = min(lastMinIndex, lastMaxIndex) - startIndex + 1
                if t > 0:
                    result += t
        return result
                
            


s = Solution() 
print(s.countSubarrays(nums = [934372,927845,479424,49441,17167,17167,65553,927845,17167,927845,17167,425106,17167,927845,17167,927845,251338,17167], minK = 17167, maxK = 927845))
