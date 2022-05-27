class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
            双关键字排序
            身高降序，k升序
            时间复杂度O(nlogn)
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res