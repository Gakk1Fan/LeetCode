class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.radius = radius

    def randPoint(self) -> List[float]:
        while True:
            rx = random.uniform(self.x - self.radius, self.x + self.radius + 0.1)
            ry = random.uniform(self.y - self.radius, self.y + self.radius + 0.1)
            if sqrt((rx - self.x) ** 2 + (ry - self.y) ** 2) <= self.radius:
                return [rx, ry]




# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()