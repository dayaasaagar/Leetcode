# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head 

        first = head
        second  = head.next
        mid = None
        
        while second and second.next:
            first = first.next
            second = second.next.next

        mid  = first.next
        first.next= None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left,right)

    def merge(self, l1: ListNode, l2:ListNode):

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:

            if l1.val<l2.val:
                current.next =l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        current.next = l1 if l1 else l2
        return dummy.next







        

