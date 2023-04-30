class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Row = len(board)
        Col = len(board[0])
        direction = [[0,1], [0,-1], [-1, 0], [1, 0]]
        def DFS(r, c):
            if r < 0 or c < 0 or r == Row or c == Col or board[r][c] != "O":
                return
            board[r][c] = "M"
            for x,y in direction:
                DFS(r + x, c + y)
        # Mark unsurrounded region o -> M
        for i in range(Row):
            for j in range(Col):
                if board[i][j] == "O" and (i in [0, Row-1] or j in [0, Col-1]):
                    DFS(i, j)

        # Flipp surrounded region o -> x
        for i in range(Row):
            for j in range(Col):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # unMark unsurrounded region M -> o
        for i in range(Row):
            for j in range(Col):
                if board[i][j] == "M":
                    board[i][j] = "O"
