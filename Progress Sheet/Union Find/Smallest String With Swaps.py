class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        size = [0]*n

        def find(member):
            if member == parent[member]:
                return member
            parent[member] = find(parent[member])
            return parent[member]
        
        def union(u, v):
            upar = find(u)
            vpar = find(v)

            if size[upar] > size[vpar]:
                parent[vpar] = upar
                size[upar] += size[vpar]
            else:
                parent[upar] = vpar
                size[vpar] += size[upar]
        
        for u,v in pairs:
            union(u, v)

        ans = list(s)
        parentSet = defaultdict(list)
        for i in range(n):
            parentSet[find(i)].append(i)

        
        for v in parentSet.values():
            swapSet = []
            for i in v:
                swapSet.append(s[i])
            swapSet.sort()

            for i in range(len(v)):
                ans[v[i]] = swapSet[i]

        return ''.join(ans)
