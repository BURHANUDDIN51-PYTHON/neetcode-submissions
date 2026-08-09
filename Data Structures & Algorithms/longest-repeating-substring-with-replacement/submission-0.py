class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        count = dict()
        l, r = 0, 0 

        while (r < len(s)):
            # Substring length
            substring_len = (r - l + 1)

            # Update frequecny 
            count[s[r]] = count.get(s[r], 0) + 1

            # Find number with highest frequency 
            maxf = max([value for _, value in count.items()])

            # Is greater then the required K 
            k_replace = substring_len - maxf 

            if k_replace <= k and substring_len > res: 
                res = substring_len
            elif k_replace > k:

                # Move the left pointer till the substring became valid 
                while ((r - l  + 1) - max([v for k, v in count.items()])) > k and l < r:
                    count[s[l]] -= 1 
                    l += 1

            r += 1


        return res