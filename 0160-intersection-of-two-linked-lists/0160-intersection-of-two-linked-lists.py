# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None
        node1 = headA
        node2 = headB
        while node1!=node2:
            if not node1:
                node1 =headB
            else:
                node1 = node1.next
            if not node2:
                node2 = headA
            else:
                node2 = node2.next

        return node1
