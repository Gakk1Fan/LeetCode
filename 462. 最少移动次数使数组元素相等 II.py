class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
            时间复杂度O(nlogn)
        """
        nums = sorted(nums)
        n = len(nums)
        mid = nums[n // 2]
        res = 0
        for x in nums:
            res += abs(mid - x)
        return res