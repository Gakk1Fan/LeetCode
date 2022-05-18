class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
            假设第k小的数是x
            要统计第k小的数 
            => 
                找到k个数>=x
        """

        def check(x):
            """
                统计乘法表中比x小的数的个数
            """
            res = 0
            for i in range(1, m + 1):
                res += min(x // i, n)
            return res

        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if k <= check(mid):
                r = mid
            else:
                l = mid + 1
        return r