from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Find the row to be searched in 
        top_row, bot_row = 0, len(matrix)-1
        while top_row <= bot_row:
            mid_row = top_row + (bot_row - top_row) // 2
            if matrix[mid_row][-1] < target:
                top_row = mid_row + 1 
            elif matrix[mid_row][0] > target:
                bot_row = mid_row - 1
            else:
                break

        # Now did the binary search for the mid row 
        if not (top_row <= bot_row):
            return False

        return self.search(matrix[top_row + (bot_row - top_row) // 2], target)

        
    def search(self, array: List[int], target: int) -> bool:
        l, r = 0, len(array) -  1

        while l <= r: 
            mid = l + (r - l) // 2
            if array[mid] < target: l = mid + 1 
            elif array[mid] > target: r = mid - 1 
            else: return True

        return False
