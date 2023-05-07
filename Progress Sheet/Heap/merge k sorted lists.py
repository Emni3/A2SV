# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if lists[i]: 
                heappush(heap, (node.val, i))
                lists[i] = lists[i].next
        ans = ListNode()
        head = ans
        while heap:
            node, i = heappop(heap)
            ans.next = ListNode(node)
            ans = ans.next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next
