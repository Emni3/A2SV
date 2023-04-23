# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        path = ""
        def DFS(root):
            nonlocal path
            if not root:
                return
                
            path += "("
            path += str(root.val)
            if not root.left and root.right:
                path += "()"
            DFS(root.left)
            DFS(root.right)
            path += ")"
        DFS(root)
        return path[1:-1]
