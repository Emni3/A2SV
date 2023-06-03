class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {i:i for i in range(len(stones))}
        rank = {i:1 for i in range(len(stones))}
        n = len(stones)
        
        def find(x):
            if parent[x] == x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep
        
        def union(x,y):  
            rep_x = find(x)
            rep_y = find(y)
            if rep_x == rep_y:
                return
            if rank[rep_x] > rank[rep_y]:
                rep_x,rep_y = rep_y,rep_x
            parent[rep_y] = rep_x
            rank[rep_x] += rank[rep_y]
        
        for i in range(n):
            for j in range(i+1,n):
                a, b = stones[i]
                c, d = stones[j]
                if a == c or b == d:
                    union(i,j)
      
        rep = set()
        ans = 0
        for i in range(n):
            s = find(i)
            if s not in rep:
                rep.add(s)
                ans += rank[s] - 1
        return ans
                
