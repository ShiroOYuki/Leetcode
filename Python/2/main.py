class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.add_val(l1, l2, 0)

    def add_val(self, l1: ListNode, l2: ListNode, addnum=0):
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        i = l1.val+l2.val+addnum
        totalNode = ListNode(i % 10)
        if not l1.next == None or not l2.next == None:
            totalNode.next = self.add_val(l1.next, l2.next, i//10)
        if i >= 10 and totalNode.next == None:
            totalNode.next = ListNode(i//10)
        return totalNode
