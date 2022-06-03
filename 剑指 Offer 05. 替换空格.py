class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ""
        for i in s:
            if i == ' ':
                res += "%20"
            else:
                res += i
        return res