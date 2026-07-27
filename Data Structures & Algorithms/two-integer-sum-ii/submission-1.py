class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer solution 
        i, j = 1, len(numbers)

        while (i < j):
            sum = numbers[i-1] + numbers[j-1]

            if sum > target: 
                j -= 1
            elif sum < target: 
                i += 1
            else: 
                return [i, j]

        
        return [-1,-1]