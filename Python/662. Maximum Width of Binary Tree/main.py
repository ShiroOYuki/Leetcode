# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        children = [root]
        m = 1
        while children:
            n = len(children)
            for _ in range(n):
                node = children.pop(0)
                children.append(node.left)
                children.append(node.right)

            for i in range(n):
                if children[i] != None:
                    break
            else:
                children = []
            children = children[i:]
            n = len(children)
            for i in range(n):
                if children[n-i-1] != None:
                    break
            children = children[:n-i]
            print(children)
            m = max(m, len(children))
            children = list(filter(lambda i: i!=None, children))
        return m

c3 = TreeNode(4)
c4 = TreeNode(5)
c1 = TreeNode(2, c3, None)
c2 = TreeNode(3, None, c4)
r = TreeNode(1, c1, c2)
print(Solution().widthOfBinaryTree(r))