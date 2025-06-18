# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current = head 
        long =0

        if not head or not head.next:
            return None

        while current:
            long +=1
            current =current.next

        index =0
        dummy = ListNode()
        new_list= dummy
        current =head


        while current:
            if long-index!=n:
                new_list.next = ListNode(current.val)
                new_list = new_list.next
            current= current.next
            index+=1
        return dummy.next




