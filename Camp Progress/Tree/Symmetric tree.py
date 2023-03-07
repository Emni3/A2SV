# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def subtree(subL, subR):
            if not subL and not subR:
                return True
            if (not subL and subR) or (subL and not subR):
                return False
            if subL.val != subR.val:
                return False
            return (subtree(subL.left, subR.right)) and (subtree(subL.right, subR.left))
        return subtree(root.left, root.right)
        
