# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """
            时间复杂度O(n)
        """
        t = root.val
        def dfs(root):
            if not root:
                return True
            return root.val == t and dfs(root.left) and dfs(root.right)
        return dfs(root)