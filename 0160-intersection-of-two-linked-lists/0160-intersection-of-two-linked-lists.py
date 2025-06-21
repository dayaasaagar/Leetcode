# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None
        

        currenta = headA
        currentb = headB

        while currenta!=currentb:

            currenta = currenta.next if currenta else headB
            currentb = currentb.next if currentb else headA
            
        return currenta
        