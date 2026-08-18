from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            col_len = len(matrix[i])

            # Check if the last element is greater than the target 
            if matrix[i][-1] >= target:
                return self.search(matrix[i], target)

        return False

    def search(self, array: List[int], target: int) -> bool:
        l, r = 0, len(array) -  1

        while l <= r: 
            mid = l + (r - l) // 2
            if array[mid] < target: l = mid + 1 
            elif array[mid] > target: r = mid - 1 
            else: return True

        return False