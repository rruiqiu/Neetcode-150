from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # matrix question
        # check diagonal, row, column
        m = len(board)
        n = len(board[0])

        for i in range(m):
            # set for duplicates
            duplicate_set = set([str(x) for x in range(1, 10)])

            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in duplicate_set:
                    duplicate_set.remove(board[i][j])
                else:
                    return False

        for i in range(n):
            duplicate_set = set([str(x) for x in range(1, 10)])
            for j in range(m):
                if board[j][i] == ".":
                    continue
                if board[j][i] in duplicate_set:
                    duplicate_set.remove(board[j][i])
                else:
                    return False

        # check the square, know 9*9, 9 loops
        for i in range(9):  # 0,1,2  3,4,5 // 3   6,7,8 ->2
            start_row = i // 3 * 3
            start_index = i % 3 * 3
            duplicate_set = set([str(x) for x in range(1, 10)])
            for j in range(9):
                row = j // 3 + start_row
                col = j % 3 + start_index
                print(row, col)
                if board[row][col] == ".":
                    continue
                if board[row][col] in duplicate_set:
                    duplicate_set.remove(board[row][col])
                else:
                    return False

        return True
