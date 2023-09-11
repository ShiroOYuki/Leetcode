import os

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        n = right - left
        t_head = head
        for _ in range(n-1):
            tail = t_head
            t_head = t_head.next  
            
        for _ in range(n):
            if t_head.next:
                n_node = tail.next
                tail.next = n_node
                t_head.next = n_node.next
                n_node.next = t_head
                node = head
                print("t_head:", t_head.val)
                while node:
                    print(node.val, end = " - " if node.next else "\n")
                    node = node.next
                t_head = t_head.next
                
        return head

res = Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
while res:
    print(res.val)
    res = res.next
    os.system("pause")
    
                
        
        