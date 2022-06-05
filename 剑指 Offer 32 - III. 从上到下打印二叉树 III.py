# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        level = 1
        while len(q):
            line = []
            for i in range(len(q)):
                t = q.popleft()
                line.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            if level % 2 == 0:
                line.reverse()
            level += 1
            res.append(line)
        return res