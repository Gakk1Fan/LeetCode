class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e = sorted(heights)
        res = 0
        for i in range(len(e)):
            if e[i] != heights[i]:
                res += 1
        return res