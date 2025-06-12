# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None

        while current is not None:

            temp = current.next
            #making current.next as previous
            current.next = prev
            #renaming current as prev
            prev= current
            #moving current
            current = temp

        return prev
            
        