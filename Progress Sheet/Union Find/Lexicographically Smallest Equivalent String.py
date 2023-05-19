class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(str)
        ans = ""
        for i in s1:
            parent[i] = i
        for i in s2:
            parent[i] = i
        
        for i in range(len(s1)):
            mini = min(parent[s1[i]],parent[s2[i]])
            reps1 = parent[s1[i]]
            reps2 = parent[s2[i]]
            for k,v in parent.items():
                if v == reps1:
                    parent[k] = mini
                if v == reps2:
                    parent[k] = mini
      
        for i in baseStr:
            if i not in parent:
                ans += i
            else:
                ans += parent[i]
        return ans
