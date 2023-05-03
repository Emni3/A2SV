class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        i,j = entrance
        queue = deque([(i,j,0)])
        visited = set()
        direc = [[0,1],[1,0],[-1,0],[0,-1]]
        def inbound(i,j):
            if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[0]) or maze[i][j] == "+":
                return False
            else:
                return True
        def edge(i,j):
            if (i == 0 or i == len(maze)-1 or j == 0 or j == len(maze[0])-1) and ([i,j] != entrance):
                return True
             
        while queue:
            length = len(queue)
            for l in range(length):
                i, j, count = queue.popleft()
                if (i,j) not in visited:
                    visited.add((i,j))
                    if maze[i][j] == "." and edge(i,j):
                        return count
                    count += 1
                    for x,y in direc:
                        if inbound(i+x, j+y):
                            queue.append((i+x, j+y, count))
        return -1
