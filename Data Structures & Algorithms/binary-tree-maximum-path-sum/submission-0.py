# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root: TreeNode):
            nonlocal res
            if not root:
                return 0
            
            left_max = dfs(root.left)
            left_max = max(left_max, 0)

            right_max = dfs(root.right)
            right_max = max(right_max, 0)

            # Compute max path sum WITH split
            res = max(res, root.val + left_max + right_max)

            # Compute max path sum WITHOUT split
            return root.val + max(left_max, right_max)
        
        dfs(root)
        return res