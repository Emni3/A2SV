class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(int)
        for i in range(n):
            d[i] = i
        def representative(x):
            while d[x] != x:
                x = d[x]
            return d[x]
		
        def union(x, y):
            repx = representative(x)
            repy = representative(y)
            if repx > repy:
                d[repy] = repx
            else:
                d[repx] = repy
    
        mini = float('inf')
        for x,y,size in roads:
            union(x,y)
        for x,y,size in roads:
            if representative(1) == representative(x) == representative(y):
                mini = min(mini, size)
        return mini
