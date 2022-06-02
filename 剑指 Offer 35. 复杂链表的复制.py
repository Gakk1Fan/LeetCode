"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        while p:
            q = Node(p.val)
            q.next = p.next
            p.next = q
            p = q.next
        
        p = head
        while p:
            if p.random == None:
                p.next.random = None
            else:
                p.next.random = p.random.next
            p = p.next.next
        
        dummy = Node(-1)
        cur =  dummy
        p = head
        while p:
            cur.next = p.next
            cur = cur.next
            p.next = p.next.next
            p  = p.next
        return dummy.next