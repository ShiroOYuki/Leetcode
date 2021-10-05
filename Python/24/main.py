class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        a = b = head
        b = head.next
        while b and a:
            t = a.val
            a.val = b.val
            b.val = t
            if not a.next or not b.next:
                break
            a = a.next.next
            b = b.next.next
        return head
