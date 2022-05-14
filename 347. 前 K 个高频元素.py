class Solution:
    """
    用字典统计nums中各个数的数量
    排序,按照key值返回。

    时间复杂度:O(nlogn)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter()
        for num in nums:
            cnt[num] += 1
        return [x[0] for x in cnt.most_common(k)]