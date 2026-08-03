from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # Create prefix and suffix for max
        n = len(height)
        prefix, suffix = [0]*n, [0]*n

        # Build the max prefix array 
        max_el = height[0]
        for i in range(1, n-1):
            if height[i] > max_el: max_el = height[i]
            prefix[i] = max_el


        # Build te max suffix array 
        max_el = height[n - 1]
        for i in range(n-2, -1, -1):
            if height[i] > max_el: max_el = height[i]
            suffix[i] = max_el


        # calculate the max water store
        max_water_store = 0
        for idx, num in enumerate(height):
            water_block = min(prefix[idx], suffix[idx]) - num
            if water_block > 0:
                max_water_store += water_block


        return max_water_store