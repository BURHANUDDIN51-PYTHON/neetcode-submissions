class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # If the t is empty 
        if len(t) == 0: return ''

        res, resLen = [-1,-1], float('inf')

        # Char Map 
        window, countT = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1


        have, need = 0, len(countT)

        l = 0 
        for r in range(len(s)):

            current_char = s[r]
            window[current_char] = window.get(current_char, 0) + 1

            # Check whether we have a element that fills the need 
            if current_char in countT and window[current_char] == countT[current_char]:
                have += 1 

            # Check whether the current substring is valid or not 
            while have == need: 

                # Update the result 
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                # Shrink the string from left pointer 
                left_char = s[l]
                window[left_char] -= 1 

                # Now check whether there is the change in the have
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1 

                l += 1 


        return s[res[0]: res[1] + 1] if resLen != float('inf') else ""
