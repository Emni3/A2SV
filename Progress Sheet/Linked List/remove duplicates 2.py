# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        distinct = ListNode()
        dist = distinct
        distinct.next = curr
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                distinct.next = curr.next
            else:
                distinct = distinct.next
            curr = curr.next
        return dist.next
