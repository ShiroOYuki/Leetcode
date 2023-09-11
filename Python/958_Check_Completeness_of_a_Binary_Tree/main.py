class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        queue = [root]
        count = 0
        while queue:
            node = queue.pop(0)
            if node == None:
                return (len(queue) - count + 1) == 0
            queue.append(node.left)
            queue.append(node.right)
            if node.left == None:
                count += 1
            if node.right == None:
                count += 1