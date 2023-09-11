# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def zigZag(node: TreeNode): # 最後會回傳三個數字，分別是左子樹長度、右子樹長度及
            if not node:
                return -1, -1, -1
            ll, lr, lm = zigZag(node.left)
            rl, rr, rm = zigZag(node.right)
            return lr + 1, rl + 1, max(lr+1, rl+1, lm, rm)
        l, r, m = zigZag(root)
        return m