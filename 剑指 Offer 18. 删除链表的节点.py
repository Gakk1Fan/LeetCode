# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre, p = dummy, head
        while p.val != val:
            pre = pre.next
            p = p.next
        pre.next = p.next
        return dummy.next