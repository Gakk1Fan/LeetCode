class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            res += (x & 1) ^ (y & 1)  # 相同为0，不同为1
            x >>= 1
            y >>= 1
        return res