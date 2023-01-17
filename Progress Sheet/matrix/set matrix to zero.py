class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col =[]
        #to get the position of the zeros
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row.append(r)
                    col.append(c)

        #to change the row of the zero
        for ro in row:
            for co in range(len(matrix[0])):
                matrix[ro][co] = 0
        #to change the column of the zero
        for ro in range(len(matrix)):
            for co in col:
                matrix[ro][co] = 0
