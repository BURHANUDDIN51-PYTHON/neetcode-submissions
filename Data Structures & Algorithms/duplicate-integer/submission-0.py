class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = dict()

        for i in nums:
            try: 
                hash_map[i] += 1
            except KeyError:
                hash_map[i] = 1

        for key, val in hash_map.items():
            if val > 1: return True
        
        return False