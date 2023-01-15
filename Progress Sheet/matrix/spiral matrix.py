class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        elements = []
        left, top = 0, 0
        right = len(matrix[0])
        bottom = len(matrix)
        
        while left < right and top < bottom:
            #collect the elements in the top row
            for i in range(left, right):
                elements.append(matrix[top][i])
            top += 1 #we visited all the top

            #collect the elements in the right most column
            for i in range(top, bottom):
                elements.append(matrix[i][right-1])
            right -= 1  #we visited all the right

            #if we have a column or a row matrix ([1, 2, 3])
            if not(left < right and top < bottom):
                break

            #collect the elements in the bottom row
            for i in range(right-1, left-1, -1):
                elements.append(matrix[bottom-1][i])
            bottom -= 1  #visited the bottom most

            #collect the elements in the left most column
            for i in range(bottom-1, top-1, -1):
                elements.append(matrix[i][left])
            left += 1  #visited the left
            
        return elements
