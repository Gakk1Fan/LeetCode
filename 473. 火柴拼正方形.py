class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        line = total / 4
        if any(num > line for num in matchsticks):
            return False
        n = len(matchsticks)
        final = (1 << n) - 1
        
        @lru_cache(None)
        def dfs(state, cur):
            if cur == line:
                cur = 0
                if state == final:
                    return True
            for i in range(n):
                if not state >> i & 1 and cur + matchsticks[i] <= line:
                    if dfs(state | 1 << i, cur + matchsticks[i]):
                        return True
            return False
        
        return dfs(0, 0)