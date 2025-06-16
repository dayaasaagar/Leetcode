# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None 
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next

            if first==second:
                first =head
                while first!=second:
                    first= first.next
                    second=second.next
                return first
        return None