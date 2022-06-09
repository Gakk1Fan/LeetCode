class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

    def pick(self) -> List[int]:
        p = []
        p.append(0)
        for t in self.rects:
            a, b, x, y = t[0], t[1], t[2], t[3]
            p.append(p[-1] + (x - a + 1) * (y - b + 1))
        n = len(p)
        k = random.randint(1, p[-1])
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if p[mid] >= k:
                r = mid
            else:
                l = mid + 1
        tmp = self.rects[r - 1]
        return [random.randint(tmp[0], tmp[2]), random.randint(tmp[1], tmp[3])]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()