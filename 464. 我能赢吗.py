class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
            记忆化搜索
            用state来表示1~maxChoosableInteger中有哪些数已经被选过
            时间复杂度O(2^n)
        """
        @lru_cache(None)
        def dfs(state: int) -> bool:
            """
                当前玩家选完后
                获胜True
                失败False
            """
            cur = sum(i + 1 for i in range(maxChoosableInteger) if state >> i & 1)  # 统计当前的总和
            for i in range(maxChoosableInteger):
                # 如果当前的数没有被使用过，并且加上这个数之后完成目标或者  加上这个数后dfs后返回False(下一个玩家选完后没有win)
                if not (state >> i & 1) and (cur + i + 1 >= desiredTotal or not dfs(state | 1 << i)):
                    return True
            return False
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return dfs(0)