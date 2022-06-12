class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(a, b):
            if len(a) != len(b):
                return False
            f, g = {}, {}
            for i in range(len(word)):
                if a[i] in f and f[a[i]] != b[i]:
                    return False
                if b[i] in g and g[b[i]] != a[i]:
                    return False
                f[a[i]] = b[i]
                g[b[i]] = a[i]
            return True

        res = []
        for word in words:
            if check(word, pattern):
                res.append(word)
        return res