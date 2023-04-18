"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node):
            if not node:
                return 0
                
            dep = 0   
            for c in node.children:
                dep = max(dep, dfs(c))
            return dep + 1
            
        return dfs(root)
            
                
