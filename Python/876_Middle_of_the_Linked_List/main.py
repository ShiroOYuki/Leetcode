class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if type(head) != ListNode:
            return False
        if not head.next:
            return head
        length = 1
        nodes = []
        while head.next:
            head = head.next
            length += 1
            nodes.append(head)
        return nodes[int(length / 2)-1]


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

head = makeList([1,2,3,4,5,6])
s = Solution()
head = s.middleNode(head)
print(head.val)
while head.next:
    head = head.next
    print(head.val)