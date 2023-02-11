# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last = head
        first = head
        curr = head
        length = 1 

        if not head or not head.next:
            return first
        if k == 0:
            return first

        while last.next:
            last = last.next
            length += 1

        k = k % length
        if k == 0:
            return first
        for i in range(length - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        last.next = first
        first = newHead

        return first
        
     
