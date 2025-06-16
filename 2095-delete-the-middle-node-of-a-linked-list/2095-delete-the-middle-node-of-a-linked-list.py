# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        first = head
        second = head
        if not head or not head.next:
            return None

        while second and second.next:
            prev = first
            first = first.next
            second = second.next.next
        
        prev.next = first.next
        return head
        i
