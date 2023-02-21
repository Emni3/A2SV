# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        size = 1
        curr = head
        while curr:
            curr = curr.next
            size += 1
        while size-1:
            ans.append(0)
            size -= 1
        curr = head
        i = 0
        while curr:
            num = curr.val

            while stack and stack[-1][1] < num:
                index, value = stack.pop()
                ans[index] = num
            stack.append((i, num))
            curr = curr.next
            i += 1

        return ans
