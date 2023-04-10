class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(row, col):
            visited.add((row,col))
            
            for x,y in mvt:
                new_row, new_col = row+x, col+y
                if in_bound(new_row, new_col) and image[new_row][new_col] == image[sr][sc] and (new_row,new_col) not in visited:
                    dfs(new_row,new_col)
            image[row][col] = newColor
       
      
        mvt = [(1,0),(-1,0), (0,1),(0,-1)]
        in_bound = lambda x,y: 0<=x <len(image) and 0<= y <len(image[0])
        visited = set()
        
        
        dfs(sr,sc)
        return image
