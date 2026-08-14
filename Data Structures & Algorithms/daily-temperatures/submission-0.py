from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # stack of tuples (element, index)
        stack = [] 

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # if stack is empty or the next element is smaller than the current top element
            if not stack or (stack and temperatures[i] <= stack[-1][1]):
                stack.append((i,temperatures[i]))
                continue

            # If the present element is greater
            j = len(stack) - 1
            while stack and stack[j][1] < temperatures[i]:
                idx, _ = stack.pop()
                res[idx] = i - idx
                j -= 1

            # Push at last 
            stack.append((i,temperatures[i]))


        return res