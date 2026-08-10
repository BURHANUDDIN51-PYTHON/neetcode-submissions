class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 > s2
        if len(s1) > len(s2):
            return False 

        # Build the substring frequency map
        s1_freq_map = {}
        for char in s1:
            s1_freq_map[char] = s1_freq_map.get(char, 0) + 1

        # Maintian a fix size sliding window over s2
        count = {}
        l = r = 0
        while (r < len(s2)):
            count[s2[r]] = count.get(s2[r], 0) + 1
            r += 1

            # Skip till we reach the s1 length
            if r < len(s1):
                continue

            # if substring == frequence map return True
            if count == s1_freq_map:
                return True


            # Else move the left pointer and adjust the count 
            if count[s2[l]] == 1: 
                del count[s2[l]]
                l += 1
            else: 
                count[s2[l]] -= 1 
                l += 1
            
        return False
