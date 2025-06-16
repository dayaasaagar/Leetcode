# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        result = []

        current = head
        if not head or not head.next:
            return None
        
        while current:
            result.append(current.val)
            current = current.next

        return True if result == result[::-1] else False