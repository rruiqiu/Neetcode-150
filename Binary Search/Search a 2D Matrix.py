class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # a simple way would be just convert them to a 1D, but that would need more space, can we do better
        # binary search on matrix
        # first search basaed on the specific row, then within the row
        # modified bs on the row, below apparoch is more robust to handle edge cases
        start, end = 0, len(matrix) - 1
        row = -1
        while start <= end:
            mid = (start + end) // 2
            if target > matrix[mid][-1]:
                start = mid + 1
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                break
        row = (start + end) // 2

        start, end = 0, len(matrix[0]) - 1
        while start <= end:
            mid = (start + end) // 2
            mid_val = matrix[row][mid]
            if mid_val == target:
                return True
            elif mid_val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
