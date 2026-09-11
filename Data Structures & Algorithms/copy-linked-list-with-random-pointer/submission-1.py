"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None

        # Old to copy logic 
        oldToCopy = {}

        # First pass
        cur = head 
        while cur: 
            oldToCopy[cur] = Node(cur.val) 
            cur = cur.next 

        # Second pass setting up the pointers
        cur = head 
        while cur: 
            copy = oldToCopy.get(cur)
            copy.next, copy.random = oldToCopy.get(cur.next), oldToCopy.get(cur.random)
            cur = cur.next 


        return oldToCopy[head]
