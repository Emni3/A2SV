# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        isPalindrome = True
        slow = head
        fast = head
        #find the mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        #reverse the half
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #print(prev)
        
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return not isPalindrome 
            left = left.next
            right = right.next
        return isPalindrome 
