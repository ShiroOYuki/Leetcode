# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        res = str(root.val)
        if (root.left): res += "(" + self.tree2str(root.left) + ")"
        if (root.right and not root.left): res += "()"
        if (root.right): res += "(" + self.tree2str(root.right) + ")"
        return res
        