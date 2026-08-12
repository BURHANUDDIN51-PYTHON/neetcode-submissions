from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Maintain a stack 
        stack = []

        # Arithmetic Operands 
        operations = {'+', '-', '*', '/'}

        for i in range(len(tokens)):

            if len(stack) >=1 and  tokens[i] in operations:

                # Pop the last two element and perform the operation 
                o1, o2 = int(stack.pop(-1)), int(stack.pop(-1))
                res = None

                # Find the operation
                match tokens[i]:
                    case '+': res = o2+o1
                    case '-':  res = o2-o1
                    case '*': res = o2*o1
                    case '/': res = o2/o1

                stack.append(res)

            else:  # Append to stack if not a operation
                stack.append(tokens[i])

        return int(stack[0]) if stack else -1