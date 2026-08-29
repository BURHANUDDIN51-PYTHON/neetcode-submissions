# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Maintain a is exist hashmap 
        isExist = set()

        temp = head 
        while temp: 
            if temp in isExist: 
                return True 
            
            isExist.add(temp)
            temp = temp.next

        return False
