# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        isBST = False
        def travers(node):
            if not node:
                return 
            travers(node.left)
            arr.append(node.val)
            travers(node.right)
            return arr
        travers(root)
        check = []
        check = sorted(arr)
        print(check)
        if arr == check and len(set(check)) == len(arr):
            return  not isBST
        return isBST
