class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            01背包问题
        """
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 == 1:
            return False
        sum //= 2
        dp = [0] * (sum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(sum, num - 1, -1):
                dp[j] |= dp[j - num]
        return bool(dp[sum])