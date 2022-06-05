class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r, = 0, len(numbers) - 1
        if numbers[r] > numbers[l]:
            return numbers[l]
        while r > l and numbers[r] == numbers[r - 1]:
            r -= 1
        if r == l:
            return numbers[l]
        while l < r:
            mid = (l + r) // 2
            if numbers[mid] >= numbers[0]:
                l = mid + 1
            else:
                r = mid
        return numbers[l]