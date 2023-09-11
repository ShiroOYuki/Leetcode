class Solution:
    def countSubarrays(self, nums: int, minK: int, maxK: int) -> int:
        result = 0
        isError = False
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                errorIndex = i
                isError = True
                break
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if isError and i > errorIndex:
                    if j >= errorIndex or i > errorIndex:
                        isError = False
                        for k in range(j+1, len(nums)):
                            if nums[k] > maxK or nums[k] < minK:
                                errorIndex = k
                                isError = True
                                break
                if (not isError or not j >= errorIndex) and (max(nums[i:j+1]) == maxK and min(nums[i:j+1]) == minK):
                    if not isError:
                        result += len(nums) - j
                    else:
                        result += errorIndex - j
                    break
        return result


s = Solution() 
print(s.countSubarrays(nums = [934372,927845,479424,49441,17167,17167,65553,927845,17167,927845,17167,425106,17167,927845,17167,927845,251338,17167], minK = 17167, maxK = 927845))
