# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        # Good to know that stack can reverse things
        
        num1 = 0
        num2 = 0
        
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next        
        
        # This is an important step on how to push values to the front
        resultSum = num1 + num2
        
        if resultSum == 0:
            return ListNode(0)

        head = ListNode(-1)
        while resultSum > 0:
            val = resultSum % 10
            resultSum //= 10
            # THis is for pushing the value VVVVVIMP
            head.val = val
            temp = head
            head = ListNode(-1)
            head.next = temp
            
            
        return head.next
