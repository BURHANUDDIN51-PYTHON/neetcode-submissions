class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force Approach
        cons_len = 0
        nums.sort()
        for i in range(len(nums)):
            seq = set()
            seq.add(nums[i])
            last_element = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == (last_element + 1):
                    seq.add(nums[j])
                    last_element = nums[j]

            if len(seq) > cons_len:
                cons_len = len(seq)

        return cons_len
