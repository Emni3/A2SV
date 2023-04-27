class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0)]) if grid[0][0]==0 else deque()
        n = len(grid)
        direction = [[1,1], [1,0], [1,-1], [-1,-1], [-1, 1], [0,1], [-1, 0], [0, -1]]
        visited = set()
        visited.add((0, 0))
        path = 0
        def inbound(row, col):
            return(0 <= row < len(grid) and 0 <= col < len(grid[0]))
        while queue:
            path += 1 
            for i in range(len(queue)):
                i,j = queue.popleft()
                
                if i == n-1 and j == n-1:
                    return path
                for l,r in direction:
                        row = i + l
                        col = j + r
                        if inbound(row, col) and grid[row][col] == 0 and (row, col) not in visited:
                            queue.append((row, col))
                            visited.add((row, col))
        return -1
