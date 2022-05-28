class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
            找到最外面的括号，删除即可
            时间复杂度O(n)
        """
        i, j, cnt = 0, 0, 0
        res = ""
        while i < len(s):
            if s[i] == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res += s[j+1: i]
                    j = i + 1
                    i = j - 1
            i += 1
        return res