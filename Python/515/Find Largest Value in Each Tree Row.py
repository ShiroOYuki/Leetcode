class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        q = [root]
        qq = []
        res = []
        m = root.val
        while q or qq:
            now = q.pop(0)
            if now:
                if now.val > m: m = now.val
                if now.left: qq.append(now.left)
                if now.right: qq.append(now.right)
            if not q:
                res.append(m)
                q = qq.copy()
                qq = []
                if q: m = q[0].val 
        return res