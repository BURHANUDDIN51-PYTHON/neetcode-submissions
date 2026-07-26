from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 1. Row filter 
        for row in range(len(board)):
            seen = set()
            for n in board[row]:
                if n in seen and n != '.':
                    return False
                seen.add(n)

        # 2. Column filter 
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                if board[row][col] in seen and board[row][col] != ".":
                    return False
                seen.add(board[row][col])


        # 3. Square box wise filter 
        from collections import defaultdict
        box_map_index = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board[row])):
                box_index = (row // 3) * 3 + (col // 3)
                if board[row][col] != ".":
                     box_map_index[box_index].append(board[row][col]) 


        # Check for duplicated in the boxes 
        for values in box_map_index.items():
            seen = set()
            for v in values[1]:
                if v in seen: 
                    return False
                seen.add(v)

        return True