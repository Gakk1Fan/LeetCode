class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # δΈθ½εζ nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return 0