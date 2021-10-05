class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int):
        if head == None:
            return
        while head.val == val:
            if head.next == None:
                return
            head = head.next
        h = preh = head
        preh = preh.next
        if preh == None:
            if h.val == val:
                return
            return head
        while preh.next != None:
            while preh.val == val:
                preh = preh.next
                if preh == None:
                    h.next = preh
                    return head
            h.next = preh
            h = h.next
            preh = preh.next
            if preh == None:
                return head
        if preh.val == val:
            h.next = None
        return head
