"""
36. Valid Sudoku
09/18/26

Approach:
Keep track of frequency for each row, col, and box (27 sets), visiting each cell
exactly once. 

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #keep track of frequencies with lists of sets
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [set() for i in range(9)]

        #loop through the board once, determine if valid in row, col, box
        for i in range(9):
            for j in range(9):
                #get info at (i, j)
                cell_value = int(board[i][j]) if board[i][j] != "." else 0
                if(cell_value == 0): continue

                #check if it has been counted before in row, col, box
                if cell_value in rows[i]: return False
                else: rows[i].add(cell_value) 
                if cell_value in cols[i]: return False 
                else: cols[j].add(cell_value)
                box_num = i // 3 + (3 * (j // 3))
                if cell_value in boxs[box_num]: return False
                else: boxs[box_num].add(cell_value)

        return True
