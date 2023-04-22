class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for c1, c2 in roads:
            graph[c1].add(c2)
            graph[c2].add(c1)

        maxi = 0
        for c1 in range(n):
            for c2 in range(c1+1, n):
                if c1 in graph[c2]:
                    minus = 1
                else:
                    minus = 0
                maxi = max((len(graph[c1]) + len(graph[c2]) - minus), maxi)
        return maxi
