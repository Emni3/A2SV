class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        ans = []
        def DFS(node, path, ans):
            if node == target:
                ans.append(path)
            for i in graph[node]:
                DFS(i, path+[i], ans)
        DFS(0, [0], ans)
        return ans
