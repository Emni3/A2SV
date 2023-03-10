# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        def divid(h):
            if not head or not h.next:
                return h
            slow = h
            fast = h
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            new_h = slow

            h1 = divid(h)
            h2 = divid(new_h)
            return merged(h1, h2)

        def merged(h1, h2):
            if not h1 and not h2:
                return
            if not h2:
                return h1
            if not h1:
                return h2

            if h1.val < h2.val:
                h1.next = merged(h1.next, h2)
                return h1
            else:
                h2.next = merged(h1, h2.next)
                return h2
        return divid(head)
