class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        a = head
        while a:
            if not a.next:
                break
            if a.val == a.next.val:
                a.next = a.next.next
            else:
                a = a.next
        return head
