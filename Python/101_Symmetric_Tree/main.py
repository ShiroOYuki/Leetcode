class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def runTree(r1:TreeNode, r2:TreeNode):
            if r1 and r2:
                if r1.val != r2.val:
                    return False
                else:
                    return runTree(r1.left, r2.right) and runTree(r1.right, r2.left)
            else:
                return r1 == r2
        return runTree(root.left, root.right)
        
        