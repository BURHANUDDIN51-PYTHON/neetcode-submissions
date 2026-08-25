from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Check if there is a rotation or not 
        if nums[0] <= nums[-1]:
            return self.binary_search(0, len(nums)-1, nums, target)

        # If there is a rotation find pivot 
        pivot = self.search_pivot(nums)

        # Find out in which section we need to search 
        if target >= nums[0]:
            return self.binary_search(0, pivot-1, nums, target)

        return self.binary_search(pivot, len(nums) - 1, nums, target)


    def search_pivot(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # Pivot is in the right half.
                l = mid + 1
            else:
                # Pivot is at mid or in the left half.
                r = mid

        return l   

    def binary_search(self, l: int, r: int, nums: List[int], target):

        while (l <= r):
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1 
            else:
                return mid
        return -1 