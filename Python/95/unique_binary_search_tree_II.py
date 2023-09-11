class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 1:
            return [TreeNode(n)]
        
        def generate(start, end):
            if start > end:
                return [None]
            
            trees = []
            
            # 生成目前規定範圍內所有的 root
            for i in range(start, end+1):
                lts = generate(start, i-1) # 生成對於當前 root 來說所有可能的左子樹
                rts = generate(i+1, end)   # 生成對於當前 root 來說所有可能的右子樹
                
                # 把當前 root 跟所有左右子樹連接，生成所有可能出現的樹
                for lt in lts:
                    for rt in rts:
                        trees.append(TreeNode(i, lt, rt))
                        
            return trees # 回傳上一個 root 底下所有可能出現的樹
        
        return generate(1, n)
        
        
res = Solution().generateTrees(1)        
print(res)