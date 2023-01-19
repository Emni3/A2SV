from collections import defaultdict 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        subBox = defaultdict(list)
        invalid = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                else:
                    if (board[row][col] in rows[row] or 
                       board[row][col] in cols[col] or
                       board[row][col] in subBox[row//3,col//3]):
                       return invalid
                    else:
                        rows[row].append(board[row][col])
                        cols[col].append(board[row][col])
                        subBox[row//3,col//3].append(board[row][col])
                        print(subBox)
                        print(cols)
                    
        return not invalid
