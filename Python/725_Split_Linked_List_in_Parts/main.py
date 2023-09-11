class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        if not head:
            return [None] * k
        now = head
        val = [now]
        while now.next:
            now = now.next
            val.append(now)
        length = len(val)
        extra = length % k
        groupLength = length // k
        result = []
        group = []
        if k >= length:
            for i in val:
                result.append([i])
            for i in range(k - length):
                result.append([])
        else:
            for i in range(length):
                group.append(val[i])
                if len(group) >= groupLength and extra == 0 or len(group) >= groupLength+1:
                    result.append(group)
                    group = []
                elif len(group) >= groupLength and extra != 0:
                    extra -= 1
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = result[i][j].val
            result[i] = self.makeList(result[i])
        return result
    
    def makeList(self, nums):
        if not nums:
            return None
        pre = None
        for i in nums:
            now = ListNode(i)
            if pre:
                pre.next = now
            else:
                head = now
            pre = now
        return head

        
s = Solution()
head = s.makeList([1, 2, 3])
result = s.splitListToParts(head, 5)
print(result)