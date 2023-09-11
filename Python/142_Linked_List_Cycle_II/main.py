class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if type(head) != ListNode:
            return None
        if not head.next:
            return None
        rec = []
        ori = head
        while head.next:
            rec.append(head)
            if head.next in rec:
                ind = rec.index(head.next)
                for _ in range(ind):
                    ori = ori.next
                return ori
            head = head.next
        return None

def makeList(nums):
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

head = makeList([-1,-7,7,-4,19,6,-9,-5,-2,-5])
pos = 6
target = head
for i in range(pos):
    target = target.next    
node = head
while node.next:
    node = node.next
node.next = target
s = Solution()
result = s.detectCycle(head)
print(result.val)

