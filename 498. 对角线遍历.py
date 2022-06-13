class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not len(mat) or not len(mat[0]):
            return []
        rows, cols = len(mat), len(mat[0])
        res = []
        for i in range(rows + cols - 1):
            if i % 2 == 0:
                j = min(i, rows - 1)
                while j >= max(0, 1 - cols + i):
                    res.append(mat[j][i-j])
                    j -= 1
            else:
                j = max(0, 1 - cols + i)
                while j <= min(i, rows - 1):
                    res.append(mat[j][i-j])
                    j += 1
        return res
