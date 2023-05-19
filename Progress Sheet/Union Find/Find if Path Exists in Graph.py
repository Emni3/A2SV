class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def representative(x):
            while d[x] != x:
                x = d[x]
            return d[x]
		
        def union(x, y):
            repx = representative(x)
            repy = representative(y)
            if rank[repx] >= rank[repy]:
                d[repx] = repy
                rank[repy] += rank[repx]
            else:
                d[repy] = repx
                rank[repx] += rank[repy]
            pass

        def connected(x, y):
            return representative(y) == representative(x)

        d = defaultdict(int)
        rank = [1 for _ in range(n)]
        for i in range(n):
            d[i] = i
        for x,y in edges:
            union(x,y) 
        
        return connected(source, destination)
