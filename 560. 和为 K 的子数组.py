class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            前缀和+两数之和
            
            时间复杂度O(n)
        """
        n, res, presum = len(nums), 0, 0
        preSums_dict = collections.defaultdict(int)
        preSums_dict[0] = 1  # 初始化前缀和为0的个数为1
        for i in range(n):
            presum += nums[i]
            res += preSums_dict[presum - k]
            preSums_dict[presum] += 1
        return res