class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First loop to get the prod value 
        prod, zero_count = 1, 0
        for num in nums: 
            if num == 0:
                zero_count += 1
                continue
            prod *= num

        # If zero is more than once causing every multi be 0.
        if zero_count > 1:
            return [0] * len(nums)


        # If zero count is 1.
        if zero_count == 1:
            return [prod if num == 0 else 0 for num in nums]
        
        # If zero count is zero
        res = []
        for num in nums: res.append(prod // num)
        return res