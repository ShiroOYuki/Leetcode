class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = [head]
        while head and head.next:
            head = head.next
            stack.insert(0, head)
        head = stack[0]
        while len(stack) > 1:
            stack[0].next = stack[1]
            stack.pop(0)
        if stack[0]:
            stack[0].next = None
        return head
    
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

head = makeList([1,2,4])
s = Solution()
head = s.reverseList(head)
print(head.val)
while head.next:
    head = head.next
    print(head.val)
        