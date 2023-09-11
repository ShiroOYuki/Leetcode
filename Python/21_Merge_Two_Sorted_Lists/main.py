class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1
        if list2.val < list1.val:
            list1, list2 = list2, list1
        if not list1.next:
            list1.next = list2
            return list1
        head = list1
        while list1.next and list2:
            if list2.val >= list1.val and list1.next and list1.val != list1.next and list2.val <= list1.next.val:
                t = [list1.next, list2.next]
                list1.next = None
                list2.next = None
                list2.next = t[0]
                list1.next = list2
                list2 = t[1]
            list1 = list1.next
        if list2 and not list1.next:
            list1.next = list2
        return head
    
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

node1 = makeList([1,2,4])
node2 = makeList([1,3,4])
s = Solution()
result = s.mergeTwoLists(node1, node2)
print(result.val)
while result.next:
    result = result.next
    print(result.val)