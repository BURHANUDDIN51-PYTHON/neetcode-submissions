class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMapping = defaultdict(int)
        for num in nums: freqMapping[num] += 1 

        # sorting the values 
        sorted_keys = sorted(freqMapping, key=lambda x: freqMapping[x], reverse=True)
        if sorted_keys:
            return sorted_keys[:k]

        return []