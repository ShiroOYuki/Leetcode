class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def addTree(node, num):
            if node.left or node.right:
                new = 0    
                if node.left:
                    new += addTree(node.left, num * 10 + node.val)
                if node.right:
                    new += addTree(node.right, num * 10 + node.val)
            else:
                return num * 10 + node.val
            return new
        return addTree(root, 0)
        
root = TreeNode(1, TreeNode(2), TreeNode(3))
s = Solution()
print(s.sumNumbers(root))