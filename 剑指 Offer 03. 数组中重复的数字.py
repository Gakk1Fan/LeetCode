class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # 不能写成 nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return 0