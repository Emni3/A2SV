class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        def inbound(i,j):
            return i < 0 or j < 0 or i == len(grid) or j == len(grid)
        
        visited = set()
        def dfs(i,j):
            if (inbound(i,j) or not grid[i][j] or (i,j) in visited):
                return

            visited.add((i,j))
            queue.append([i,j])
            for x,y in direction:
                dfs(i + x, j + y)
                
        def bfs():
            path = 0
            while queue:
                for l in range(len(queue)):
                    r, c = queue.popleft()
                    for x, y in direction:
                        if inbound(r+x, c+y) or (r+x, c+y) in visited:
                            continue
                        if  grid[r+x][c+y]:
                            return path
                        queue.append([r+x, c+y])
                        visited.add((r+x, c+y))
                path += 1
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()
