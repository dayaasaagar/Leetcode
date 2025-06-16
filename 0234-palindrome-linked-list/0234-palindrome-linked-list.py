# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


        #find the middle
        first= head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
        
        prev = None
        while first:
            temp = first.next
            first.next = prev
            prev = first
            first = temp
        #now prev will be pointing to the starting of the second half

        start= head
        half = prev

        while half:

            if start.val!=half.val:
                return False
            
            start= start.next
            half= half.next
        return True