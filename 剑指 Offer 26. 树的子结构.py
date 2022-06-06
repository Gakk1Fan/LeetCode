# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        
        def dfs(p, q):
            if not q:
                return True
            if not p or p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)