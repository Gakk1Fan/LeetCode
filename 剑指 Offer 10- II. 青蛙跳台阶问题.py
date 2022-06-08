class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        while n > 0:
            c = a + b
            a = b
            b = c
            n -= 1
        return a % 1000000007