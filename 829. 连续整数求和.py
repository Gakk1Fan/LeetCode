class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        for b in range(1, isqrt(2*n) + 1):
            if 2 * n % b == 0 and (2 * n / b - (b - 1)) % 2 == 0:
                res += 1
        return res