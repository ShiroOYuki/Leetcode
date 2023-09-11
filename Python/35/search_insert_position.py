class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        head = len(nums)
        tail = 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while True:
            index = int((tail+head)/2)
            current = nums[index]
            # print(index, current, nums[index-1])
            if current >= target:
                if nums[index-1] < target:
                    break
                head = index
            if current < target:
                tail = index
        return index
    
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums = [1,3,5,6], target = 7))