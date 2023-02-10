# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        small = ListNode()
        great = ListNode()
        lastG = great
        lastS = small
       
        while curr:
            if curr.val < x:
                lastS.next = curr
                lastS = lastS.next
            else:
                lastG.next = curr
                lastG = lastG.next
            curr = curr.next
        
        lastS.next = great.next
        lastG.next = None
        return small.next
