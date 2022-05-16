# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            思路：
                遍历每一个结点，计算左子树和右子树的高度，更新res
            
            时间复杂度O(n)
        """
        self.res = 0
        if not root:
            return 0
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.res = max(self.res, l + r)
            return max(l, r) + 1
        
        dfs(root)
        return self.res