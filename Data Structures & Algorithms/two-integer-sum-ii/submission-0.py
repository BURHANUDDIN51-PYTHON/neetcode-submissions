class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hash_set = {}

        for i, num in enumerate(numbers, start=1):
            diff = target - num
            if diff in hash_set: 
                return [min(hash_set[diff], i), max(hash_set[diff], i)]
            hash_set[num] = i

        return [-1,-1]
