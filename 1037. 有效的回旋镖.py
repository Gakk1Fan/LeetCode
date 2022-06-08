class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def cross(x1, y1, x2, y2):
            return x1 * y2 - x2 * y1
        
        if cross(points[2][0] - points[0][0], points[2][1] - points[0][1], points[1][0] - points[0][0], points[1][1] - points[0][1]) != 0:
            return True
        return False