# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def travers(node):
            if not node:
                return [0, 0] # [total, count]
            left = travers(node.left) 
            right = travers(node.right)
            total = left[0] + right[0] + node.val
            count = left[1] + right[1] + 1
            return [total, count]
        if not root:
            return 0
        t, c = travers(root)
        

        if (t//c) == root.val:
            ans += 1
        l= self.averageOfSubtree(root.left)
        r = self.averageOfSubtree(root.right)
        ans += l+r
        return ans
