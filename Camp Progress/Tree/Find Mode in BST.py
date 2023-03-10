# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()
        ans = []
        def travers(node):
            if not node:
                return
            count[node.val] += 1
            travers(node.left)
            travers(node.right)
        
        travers(root)

        mx= sorted(count.values())[-1]
        for i in count:
            if count[i] == mx:
                ans.append(i)
        
        return ans
