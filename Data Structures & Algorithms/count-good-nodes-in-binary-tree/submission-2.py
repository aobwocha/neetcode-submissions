# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, max_value: int):
            if not root:
                return 0
            
            res = 1 if root.val >= max_value else 0
            max_value = max(max_value, root.val)

            res += dfs(root.left, max_value)
            res += dfs(root.right, max_value)

            return res
        
        return dfs(root, root.val)
        