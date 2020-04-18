# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        pointer = result
        summation = 0
        
        # She why are we doing to next node
        while l1 or l2:
            if l1 is not None:
                summation += l1.val
                l1 = l1.next
            if l2 is not None:
                summation += l2.val
                l2 = l2.next
            result.next = ListNode(summation % 10)
            result = result.next
            summation //= 10
        # This is very imp see why
        if summation > 0:
            result.next = ListNode(summation % 10)
        return pointer.next
