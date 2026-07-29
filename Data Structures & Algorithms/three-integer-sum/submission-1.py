class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
       
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while (j < k):
                summation = nums[i] + nums[j] + nums[k]

                if summation > 0:
                    k -= 1
                elif summation < 0:
                    j += 1 
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # Move the left pointer
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1


        return res