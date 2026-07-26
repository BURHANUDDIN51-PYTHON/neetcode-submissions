class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass solution 
        indices = dict()
        for i, val in enumerate(nums):
            diff = target - val
            if diff in indices and indices[diff] != i:
                return [indices[diff], i]
            indices[val] = i

        return []