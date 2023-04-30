# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def pre(arr):
            if not arr:
                return None
            root = TreeNode(arr[0])
            i = 1
            while i < len(arr) and arr[i] < root.val:
                i += 1
            root.left = pre(arr[1:i])
            root.right = pre(arr[i:])    
            return root
        
        return pre(preorder)
