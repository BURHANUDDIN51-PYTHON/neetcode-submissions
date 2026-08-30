# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Divide the linked list into two halves by finding middle
        fast,slow = head, head
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        # Reverse the second half 
        temp = slow
        prev = None 
        while temp: 
            nextPointer = temp.next 
            temp.next = prev 
            prev = temp
            temp = nextPointer

        # Now merge both the half such that it will get the order 
        i = head.next
        j = prev 
        index = 0
        pointer = head
        while i and j:
            if index % 2: 
                pointer.next = i
                pointer = i
                i = i.next 
            else: 
                pointer.next = j
                pointer = j
                j = j.next
            index += 1

        # Add the remaining values 
        while i and i != slow: 
            pointer.next = i
            pointer = i
            i = i.next

        