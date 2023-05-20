class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {}
        for i in range(26):
            rep[chr(97 + i)] = chr(97 + i)
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            rep[yrep] = rep[xrep]
            
        for i in equations:
            if i[1] == "=":
                union(i[0], i[3])
        for i in equations:
            if i[1] != "=":
                if find(i[0]) == find(i[3]):
                    return False
        return True
