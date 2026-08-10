# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
            
            right_child = node.right #1
            left_child = node.left #2

            node.left = right_child #1
            node.right = left_child #2

            dfs(node.left)
            dfs(node.right)
        
            return node


        return dfs(root)