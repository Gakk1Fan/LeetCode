class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
            时间复杂度O(n)
            相同的元素最多相隔两位[9,4,5,9]
        """
        for i in range(1, len(nums)):
            t = nums[i]
            if i > 0 and nums[i-1] == t:
                return t
            if i > 1 and nums[i-2] == t:
                return t
            if i > 2 and nums[i-3] == t:
                return t
        return -1