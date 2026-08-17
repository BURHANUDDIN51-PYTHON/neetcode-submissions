from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Maximum area 
        max_area = 0

        # Maintain a tuple stack with the height and index
        stack = []

        # loop to have the right boundary 
        for idx, height in enumerate(heights):

            # Check if the bar is first one or increasing 
            if stack and stack[-1][1] <= height:
                stack.append((idx, height))
                continue

            # If the current element is less than the top of stack 
            left_boundary = idx 
            while stack and stack[-1][1] > height:

                # Pop the top element
                i, h = stack.pop()

                # Calculate the max area 
                max_area = max(max_area, (h * (idx - i)))

                # Update the start 
                left_boundary = i

            # Add the value to the stack 
            stack.append((left_boundary, height))

        # Empty stack if values still present 
        while stack: 
            i, h = stack.pop()
            max_area = max(max_area, (h * (len(heights) - i)))
        
        return max_area
