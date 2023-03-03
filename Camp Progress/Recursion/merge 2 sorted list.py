class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        def merge(first, second):
            tail = None
            if not first:
                return second
            elif not second:
                return first
            
            if first.val > second.val:
                tail = second
                tail.next = merge(first, second.next)
            else:
                tail = first
                tail.next = merge(first.next, second)
            
            return tail

        return merge(list1, list2)
