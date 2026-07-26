class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        mappings = {}
        for i in s: 
            try:
                mappings[i] += 1
            except KeyError:
                mappings[i] = 1  

        for j in t: 
            if j in mappings:
                if mappings[j] > 1:
                    mappings[j] -= 1
                else:
                    del mappings[j]
        
        return True if not mappings else False
                 


