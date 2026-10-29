class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat first col as an array, bisect to find
        # smallest number >= target
        lo, hi = 0, len(matrix)
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target:
                lo = mid + 1
            else:
                hi = mid

        # Target smaller than everything in first col
        if not lo > 0: return False
        # Target in first col
        if matrix[lo - 1][0] == target: return True

        row = lo - 1
        lo, hi = 0, len(matrix[0])
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        
        return lo > 0 and matrix[row][lo - 1] == target



