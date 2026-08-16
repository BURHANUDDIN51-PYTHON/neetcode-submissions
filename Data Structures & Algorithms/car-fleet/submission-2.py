from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        # Tuple array with position and time to reach the target
        ps = sorted(zip(position, speed), reverse=True, key=lambda x: x[0])


        for p, s in ps:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)