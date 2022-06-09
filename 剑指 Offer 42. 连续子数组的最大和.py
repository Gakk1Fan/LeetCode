class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, s = -1000, 0
        for num in nums:
            if s <= 0:
                s = num
            else:
                s += num
            res = max(res, s)
        return res