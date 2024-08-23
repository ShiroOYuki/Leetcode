# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.dfs(root)
        return 0
                
    def dfs(self, node: TreeNode):
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)
        if not node.left and not node.right:
            print(node.val, "\tLeaf")
        else:
            print(node.val, "\tParent")
                    
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

s = Solution()
print(s.countPairs(root, 3))
                