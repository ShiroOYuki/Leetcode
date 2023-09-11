import os
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        index = int(len(nums)/2)
        current = nums[index]
        if current == target:
            return index
        elif current > target:
            result = self.search(nums[:index],target)
            index = index - len(nums[:index]) + result
        else:
            result = self.search(nums[index:],target)
            index += result
        if result == -1:
            return result
        return index
    
    def search2(self, nums: list[int], target: int) -> int:
        head = 0
        tail = len(nums)
        index = int((tail+head)/2)
        current = nums[index]
        while current != target and tail != head:
            if tail == head+1 and current != target:
                return -1
            if current > target:
                tail = index
            elif current < target:
                head = index
            index = int((tail+head)/2)
            current = nums[index]
        return index 
    
if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 3
    print(s.search2(nums,target))