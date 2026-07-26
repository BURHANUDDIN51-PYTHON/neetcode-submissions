from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = list()

        is_added_group = {n:False for n in strs}

        # Maintian two pointers 
        for i, i_str_val in enumerate(strs):
            anagram_group = [i_str_val]

            # Check already being added in the group 
            if i_str_val in is_added_group and is_added_group[i_str_val]:
                continue

            # Add to the group
            is_added_group[i_str_val] = True

            for j, j_str_val in enumerate(strs[i+1:], start=i+1):
                if self.isAnagram(i_str_val, j_str_val):
                    anagram_group.append(j_str_val)
                    is_added_group[j_str_val] = True
            groups.append(anagram_group)

        return groups

    def isAnagram(self, s: str, t:str) -> bool:

        if len(s) != len(t):
            return False
            
        mapping = {}     

        # Build the mappings
        for i in s:
            try:
                mapping[i] += 1
            except KeyError:
                mapping[i] = 1

        # Check whether anagram is or not 
        for j in t:
            if j in mapping:
                if mapping[j] == 1:
                    del mapping[j]
                else:
                    mapping[j] -= 1

        return True if not mapping else False 



        
