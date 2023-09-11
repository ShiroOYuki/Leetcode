
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        vals = [head.val]
        while head.next:
            head = head.next
            vals.append(head.val)
        def getRoot(l):
            if not l: return
            mid = len(l) // 2
            head = TreeNode(l[mid])
            head.left = getRoot(l[:mid])
            head.right = getRoot(l[mid+1:])
            return head
        head = getRoot(vals)
        return head
            
        
         
        