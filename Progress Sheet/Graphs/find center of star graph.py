class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(int)
        for i in range(len(edges)):
            d[edges[i][0]] += 1
            d[edges[i][1]] += 1
        for i in d:
            if d[i] == len(edges):
                return i

        
