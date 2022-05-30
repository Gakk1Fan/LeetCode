# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
            如果节点是叶子节点，返回它对应的数字sum
            如果节点是非叶子节点，返回它的左子树和右子树对应的结果之和
            时间复杂度O(n)
            空间复杂度O(n)
        """
        def dfs(root, x):
            x = x * 2 + root.val
            if not root.left and not root.right:
                return x
            res = 0
            if root.left:
                res += dfs(root.left, x)
            if root.right:
                res += dfs(root.right, x)
            return res

        return dfs(root, 0)