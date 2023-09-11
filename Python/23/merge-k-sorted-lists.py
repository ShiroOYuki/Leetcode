class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLists(node, text=""):
    print(text, end = ": ")
    print(node.val, end="->")
    while node.next:
        node = node.next
        print(node.val, end="->")
    print()

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        
        # del NULL value
        i = 0
        while i < len(lists):
            if not lists[i]:
                lists.pop(i)
            else:
                i += 1
        
        # detect length < 1
        n = len(lists)
        if n < 1:
            return
        
        # link all nodes
        prev = None
        for head in lists:
            node = head
            if prev:
                prev.next = node
            while node and node.next:
                node = node.next
                n += 1
            prev = node

        # sort
        tail = lists[0]
        for i in range(n):
            head = lists[0]
            for j in range(i):
                if tail.val < head.val:
                    tail.val, head.val = head.val, tail.val
                head = head.next
            tail = tail.next
        return lists[0]
        

n3 = ListNode(5)
n2 = ListNode(4, n3)
n1 = ListNode(1, n2)

l = [n1]

n3 = ListNode(4)
n2 = ListNode(3, n3)
n1 = ListNode(1, n2)

l.append(n1)
    
s = Solution()
s.mergeKLists(l)
    