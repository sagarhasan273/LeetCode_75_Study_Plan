# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(node):
            if not node:
                return -1
            
            left = 1 + dfs(node.left)
            
            right = 1 + dfs(node.right)
            
            res[0] = max(res[0], left+right)
            
            return max(left, right)
        
        dfs(root)
        return res[0]