class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if not inorder:
            return
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root_index = inorder.index(postorder[-1])
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        left_postorder = postorder[:len(postorder) - 1 - len(right_inorder)]
        right_postorder = postorder[len(postorder) - 1 - len(right_inorder):-1]
        root = TreeNode(postorder[-1], self.buildTree(left_inorder, left_postorder), self.buildTree(right_inorder, right_postorder))
        return root    

s = Solution()
s.buildTree([1,2,3], [1,2,3])