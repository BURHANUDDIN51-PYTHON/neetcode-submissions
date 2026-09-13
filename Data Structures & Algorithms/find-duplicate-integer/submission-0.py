class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 
        # Find the cycle intersection
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break 

        # Find the duplicate number 
        slow2 = 0 
        while True:
            slow, slow2 = nums[slow], nums[slow2]
            if slow == slow2: return slow