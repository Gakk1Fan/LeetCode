# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
            1. 从根节点 root 开始，比较当前 cur 节点的值和节点 p 的值的大小关系
            2. 如果当前 cur 节点的值小于或等于节点 p 的值，那么比节点 p 的值大的节点应该在它的右子树
            3. 如果当前 cur 节点的值大于节点 p 的值，那么当前节点有可能是 p 的下一个节点，还需要判断当前 cur 节点的左节点是否满足以上条件


            时间复杂度O(n)
            空间复杂度O(1)
        """
        if not root:
            return None
        
        cur, res = root, None
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res