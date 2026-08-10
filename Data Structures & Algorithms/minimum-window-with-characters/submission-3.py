class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_len = len(s) + 1
        best_start = 0

        # Build a frequency map
        char_map = {}
        for char in t:
            char_map[char] = char_map.get(char, 0) + 1 


        # Find the first left pointer
        l = 0
        while l < len(s) and s[l] not in char_map:
            l += 1

        r = l

        # Maintain a count dict of the substring
        count = {}
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            # Loop to check whether the current substring is valid or not 
            is_valid = True
            for c in char_map:
                if c not in count or (c in count and count[c] < char_map[c]):
                    is_valid = False
                    break

            # If valid then update result 
            if is_valid:

                while l <= r:
                    current_char = s[l]

                    # Check if the char in char_map
                    if current_char not in char_map:
                        count[current_char] -= 1
                        l += 1 
                
                    elif count[current_char] > char_map[current_char]:
                        count[current_char] -= 1
                        l += 1 

                    else: 
                        break

                # Update the result 
                if (r-l+1) < best_len:
                    best_len = r-l+1
                    best_start = l

            r += 1 


        if best_len == len(s) + 1:
            return ''
            
        return s[best_start:best_start+best_len]
