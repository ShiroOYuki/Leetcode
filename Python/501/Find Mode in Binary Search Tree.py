from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        freq = defaultdict(int)
        q = [root]
        m = -1
        res = []
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            freq[node.val] += 1
            if freq[node.val] > m:
                m = freq[node.val]
        for i in freq.keys():
            if freq[i] == m:
                res.append(i)
        return res
        
        
print(Solution().findMode(TreeNode(2, TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(3, TreeNode(4))))))