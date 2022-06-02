# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        while head:
            r = head.next
            head.next = dummy.next
            dummy.next = head
            head = r
        return dummy.next