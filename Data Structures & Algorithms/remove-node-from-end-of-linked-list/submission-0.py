from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get the length of the list 
        length = 0 
        temp = head 
        while temp: 
            temp = temp.next 
            length += 1

        target = length - n # Target Index 

        # If the target is first element 
        if target == 0: 
            return head.next 

        # If the target index is greated than 0 
        index = 0 
        tmp = head
        while tmp: 
            if index == target -1: 
                tmp.next = tmp.next.next
            tmp = tmp.next 
            index += 1 

        return head