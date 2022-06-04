class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] > mid:
                r = mid - 1
            else:
                l = mid
        if nums[l] == l:
            return l + 1
        else:
            return l