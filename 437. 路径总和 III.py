# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            前缀和
                用哈希表维护从根节点到当前结点的距离
            时间复杂度O(n)
            空间复杂度O(n)
        """
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        self.res = 0

        def dfs(root, targetSum, cur):
            if not root:
                return
            cur += root.val
            self.res += cnt[cur - targetSum]
            cnt[cur] += 1
            dfs(root.left, targetSum, cur)
            dfs(root.right, targetSum, cur)
            cnt[cur] -= 1
        
        dfs(root, targetSum, 0)
        return self.res