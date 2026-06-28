import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seenRows = collections.defaultdict(set)
        seenCols = collections.defaultdict(set)
        seenSquares = collections.defaultdict(set)

        for i in range(0,9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in seenRows[i] or 
                    board[i][j] in seenCols[j] or 
                    board[i][j] in seenSquares[(i//3, j//3)]):
                    return False
                seenRows[i].add(board[i][j])
                seenCols[j].add(board[i][j])
                seenSquares[(i//3, j//3)].add(board[i][j])

        return True

     