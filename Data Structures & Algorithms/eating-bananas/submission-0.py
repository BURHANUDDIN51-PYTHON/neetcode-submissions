from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Mininum K 
        min_k = 0

        l, r = 1, max(piles)

        while l <= r: 
            mid = l + (r - l) // 2

            # Calculate the hour required with this k as mid
            hours = 0
            for pile in piles: 
                hour = pile // mid 
                hours += hour if pile % mid == 0 else hour + 1 

            if hours > h:
                l = mid + 1 
            elif hours <= h: 
                min_k = mid
                r = mid - 1

        return min_k