class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            时间复杂度O(n)
        """
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] *= -1
        res = []
        # 如果nums[i] > 0 说明i + 1不存在
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res