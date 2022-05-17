class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        """
            数组中找到第一个右边比它更大数
            时间复杂度O(n)
        """
        n = len(t)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and t[i] >= t[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res