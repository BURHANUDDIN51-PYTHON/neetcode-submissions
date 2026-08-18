from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Check if the array is rotated or not 
        if nums[0] <= nums[-1]:
            return nums[0]

        # If the array is rotated 
        left, right = 0, len(nums) - 1
        while (left < right):
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid

            # If we are in sorted array 
            elif nums[left] < nums[right]:
                while left > 1 and nums[left] > nums[left - 1]:
                    left -= 1
                break
                

        return nums[left]