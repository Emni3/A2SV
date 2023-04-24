# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sum_ = []
        def preorderTrav(node, prev):
            if not node:
                return
            if node and not node.left and not node.right:
                sum_.append("".join(prev+[str(node.val)]))
            preorderTrav(node.left, prev+[str(node.val)])
            preorderTrav(node.right, prev+[str(node.val)])
        preorderTrav(root, [])

        return sum([int(i) for i in sum_])
