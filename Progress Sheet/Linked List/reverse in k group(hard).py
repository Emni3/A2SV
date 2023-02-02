# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        rem = size % k
        tail = None
        count = 0
        res = None
        curr = head
        ans = None
        prev = None
        i = 0
        while i < size-rem:
            if not ans:
                nex = curr.next
                curr.next = ans
                ans = tail = curr
                curr = nex
            else:
                nex = curr.next
                curr.next = ans
                ans = curr
                curr = nex
            if count == (k-1):
                if prev:
                    prev.next = ans
                else:
                    res = ans
                prev = tail
                ans = None
                tail = None
                count = 0
            else:
                count += 1
            i += 1
        if rem != 0:
            i = 0
            trav = res
            while i < (size-rem-1):
                trav = trav.next
                i += 1
            trav.next = curr
        return res
