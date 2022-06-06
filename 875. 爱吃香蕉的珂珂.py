class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, k):
            res = 0
            for pile in piles:
                res += (pile + k - 1) // k
            return res

        l, r = 1, 1000000000
        while l < r:
            mid = (l + r) // 2
            if check(piles, mid) <= h:
                r = mid
            else:
                l = mid + 1
        return r