# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        maxi = 0
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        i = 0
        j = len(arr) - 1
        while i < j:
            pairSum = arr[i] + arr[j]
            i += 1
            j -= 1
            if pairSum > maxi:
                maxi = pairSum
        return maxi
            
