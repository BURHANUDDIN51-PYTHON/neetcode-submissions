class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        longest_substring = 1
        seen = {s[0]}
        l, r = 0, 1
        while (r < len(s)):
            # Check if seen 
            if s[r] in seen: 
                longest_substring = max(longest_substring, len(seen))

                # move the left pointer till the first occurence 
                while not s[l] == s[r] and l < r:
                    seen.remove(s[l])
                    l +=  1 
                l += 1

            seen.add(s[r])
            r += 1
        
                          
        return max(longest_substring, len(seen))