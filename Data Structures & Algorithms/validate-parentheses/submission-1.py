class Solution:
    def isValid(self, s: str) -> bool:

        # Maintain a stack 
        stack = []

        # Opening and closing bracket set 
        close_bracket_mapping = {
            ')': '(',
            '}' : '{',
            ']' : '['
        }        

        # Loop over the string 
        for i in range(len(s)):
            if s[i] not in close_bracket_mapping: 
                stack.append(s[i])

            # If it is a closing bracket and their is a corresponding opening bracket
            elif stack and stack[-1] == close_bracket_mapping[s[i]]:
                stack.pop(-1)

            # If closing bracket but not a corresponding opening bracket
            else:
                return False
            

        return True if len(stack) == 0 else False