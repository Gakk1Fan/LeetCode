class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for num in nums:
            if (target - num) in d:
                return [num, target - num]
            d[num] = 1
        return []