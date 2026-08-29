from typing import List 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        totals = len(A) + len(B)
        half = totals // 2

        # Choose the smaller array 
        if len(B) < len(A): A, B = B, A


        # Binary Search over A 
        l, r = 0, len(A)-1
        while True: 
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Arigth = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Brigth = B[j+1] if (j+1) < len(B) else float("infinity")


            # If partition is valid 
            if Aleft <= Brigth and Bleft <= Arigth: 
                # If Odd 
                if totals % 2: 
                    return min(Arigth, Brigth)
                else: 
                    return (max(Aleft, Bleft) + min(Arigth, Brigth)) / 2

            # If Partition is not valid 
            elif Aleft > Brigth:
                r = i - 1
            else: 
                l = i + 1