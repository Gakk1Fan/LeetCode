class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp

"""
    bits[i]表示i的二进制中1的个数，那么bits[i-1]就是bits[i]拿掉一个1之后的值，i & (i - 1)就是去掉最低位的一个1
    ==> bits[i]可以通过bits[i-1]获得

    状态转移方程:
    dp[i] = dp[i & (i - 1)] + 1

    复杂度: 时间复杂度O(n)。空间复杂度是O(1)
"""