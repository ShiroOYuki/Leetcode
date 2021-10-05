class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# head = [1, [2, [3, [4, [5]]]]]
# fast = [1, [2, [3, [4, [5]]]]]
# slow = [1, [2, [3, [4, [5]]]]]
# n = 2

# fast = [3, [4, [5]]]

# fast = [5]
# slow = [3, [4, [5]]]

# slow.next = [5]

# slow = [3, [5]]
