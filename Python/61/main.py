class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        ca = head
        c = 1
        while ca:
            if not ca.next:
                break
            ca = ca.next
            c += 1
        k = k % c
        for i in range(k):
            a = head.next
            b = head
            while a:
                if not a.next:
                    break
                a = a.next
                b = b.next
            b.next = None
            a.next = head
            head = a
        return head
