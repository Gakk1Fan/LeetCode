class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
            排序后二分
            
            时间复杂度(nlogn)
        """
        n = len(intervals)
        if n == 1:
            return [-1]
        
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()

        res = [-1] * n
        for i in range(n):
            l, r = i, n - 1
            while l < r:
                mid = (l + r) // 2
                if intervals[mid][0] < intervals[i][1]:
                    l = mid + 1
                else:
                    r = mid
            if intervals[r][0] >= intervals[i][1]:
                res[intervals[i][2]] = intervals[r][2]
        return res