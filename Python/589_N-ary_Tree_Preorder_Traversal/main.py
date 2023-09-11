# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list:
        if not root:
            return root
        l = []
        def run(root: Node):
            l.append(root.val)
            if root and root.children:
                for node in root.children:
                    run(node)
        run(root)
        return l
        
