class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = defaultdict()
        size = len(edges)
        for i in range(1, size+1):
            rep[i] = i
        
        def representative(x):
            if rep[x] == x:
                return x
            rep[x] = representative(rep[x])
            return rep[x]

        for x, y in edges:
            repx = representative(x)
            repy = representative(y)
            if repx == repy:
                return [x, y]
            rep[repx] = repy 
        return []
        
