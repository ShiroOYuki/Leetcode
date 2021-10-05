class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Question request:Binary Tree Inorder Traversal(left,root,right)
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return
        if not root.left and not root.right:
            return [root.val]
        self.ans = []

        def find(node):
            if not node:
                return
            find(node.left)  # left first
            self.ans.append(node.val)  # than root
            find(node.right)  # last right
        find(root)
        return self.ans


"""main.py
        2
    3        
1

1,3
2,3

2,1
"""
