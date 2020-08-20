# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dic = {}
        curr = head
        n = 0
        if head == None:
            return head
        while curr:
            dic[n] = curr
            curr = curr.next
            n += 1
        res = ListNode(0)
        curr = res
        for i in range(n//2 + 1):
            res.next = dic[i]
            res.next.next = dic[n-i-1]
            res = res.next.next
        res.next = None
        return curr.next
