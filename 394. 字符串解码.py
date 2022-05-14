class Solution:
    """
        用栈保存当前字符串需要重复的次数和计算这个字符串（也就是[之前）之前字符串的结果
        时间复杂度O(n)
    """
    def decodeString(self, s: str) -> str:
        stack, mutil, res = [], 0, ""
        for c in s:
            if c == '[':
                stack.append([mutil, res])  # 保存上次层的系数和到'['为止的整个字符串
                mutil, res = 0, ""
            elif c == ']':
                t_mutil, t_res = stack.pop()
                res = t_res + t_mutil * res
            elif '0' <= c <= '9':
                mutil = mutil * 10 + int(c)
            else:
                res += c
        return res