# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        if len(data) <= 1:
            return True
        data = self.search(root,[])
        if sorted(data) == data:
            for i in range(1,len(data)):
                if data[i] in data[i+1:] or data[i] in data[:i]:
                    return False
            return True
        return False
    
    def search(self,node,data):
        if node:
            self.search(node.left,data)
            data.append(node.val)
            self.search(node.right,data)
        return data