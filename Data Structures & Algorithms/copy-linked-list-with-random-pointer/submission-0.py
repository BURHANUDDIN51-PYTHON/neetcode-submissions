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

        # Create a new Linked List with hashmap 
        node_hash = {} 
        copy_head =  Node(head.val)
        node_hash[head] = copy_head
        # Create the copy without considering the random pointer 
        # First Pass 
        temp, copy_temp = head.next, copy_head
        while temp: 
            new_node = Node(temp.val)
            copy_temp.next = new_node
            copy_temp = new_node

            # Hashamp entry 
            node_hash[temp] = new_node

            # Move the pointer 
            temp = temp.next 


        # Second pass to adjust the random pointer 
        tmp, copy_tmp = head, copy_head
        while tmp: 
            random_pointer = node_hash.get(tmp.random, None)
            copy_tmp.random = random_pointer

            tmp = tmp.next
            copy_tmp = copy_tmp.next 

        return copy_head