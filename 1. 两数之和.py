class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            x = target - nums[i]
            if x in d:
                return [d[x], i]
            d[nums[i]] = i
        return []