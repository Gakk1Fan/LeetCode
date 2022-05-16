# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
            按照中->右->左的顺序遍历
            记录值，然后累加并修改值
        """
        self.sum = 0
        def dfs(root):
            if not root:
                return None
            dfs(root.right)
            self.sum += root.val
            root.val = self.sum
            dfs(root.left)
            return root
        dfs(root)
        return root