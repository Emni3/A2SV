class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        generated = [[0 for i in range(len(grid)-2)] for j in range(len(grid)-2)]
        # iterate through the 3x3 grid and select a number as a maximum
        for row in range(len(grid)-2):
            for col in range(len(grid)-2):
                max_num = grid[row][col]
                # compare the selected num with the rest of the 3x3 grid
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        max_num = max(max_num, grid[i][j])
                generated[row][col] = max_num
               
        return generated
