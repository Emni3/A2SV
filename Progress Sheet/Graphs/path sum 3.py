# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        d = defaultdict(int)
        d[0] += 1
        def travers(root,total):
            nonlocal ans
            if not root:
                return 
            total += root.val
            ans += d[total - targetSum]
            d[total] += 1
        
            travers(root.left, total)
            travers(root.right, total)
            d[total] -= 1
            
        travers(root,0)
        return ans
