class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # brute force approach 
        for i in range(len(nums)):
            prod = None
            for j in range(len(nums)):
                if i != j:
                    try:
                        prod *= nums[j]
                    except TypeError:
                        prod = nums[j]
            res.append(prod)

        return res