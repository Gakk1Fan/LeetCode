class Solution:
    """
    依次枚举，使用叉积公式计算三角形面积
    """
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def cross(x1, y1, x2, y2):
            return x1 * y2 - x2 * y1
        
        def area(l1, l2, l3):
            return cross(l3[0] - l1[0], l3[1]- l1[1], l2[0] - l1[0], l2[1] - l1[1])
        
        res = 0
        for a in points:
            for b in points:
                for c in points:
                    res = max(res, abs(area(a, b, c)))
        return res / 2