# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # breath first search
        ans = []
        level = defaultdict(list)
        def travers(node, depth):
            if not node:
                return
            level[depth].append(node.val)
            
            travers(node.left, depth+1)
            travers(node.right, depth+1)
            
        travers(root, 0)
        for k, v in level.items():
            ans.append(v)
        
        return ans
