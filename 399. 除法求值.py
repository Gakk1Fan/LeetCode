class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
            时间复杂度O(n^3)
            Flyod算法
        """
        vers = set()
        d = collections.defaultdict(int)
        for i in range(len(equations)):
            a, b = equations[i]
            d[(a, b)] = values[i]
            d[(b, a)] = 1 / values[i]
            vers.add(a)
            vers.add(b)

        for k in vers:
            for i in vers:
                for j in vers:
                    if d[(i, k)] and d[(j, k)]:
                        d[(i, j)] = d[(i, k)] * d[(k, j)]
        
        res = []
        for a, b in queries:
            if not d[(a, b)]:
                res.append(-1)
            else:
                res.append(d[(a, b)])
        return res