class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = {_:[] for _ in range(len(nums) + 1)}

        for num in nums: count[num] = 1 + count.get(num, 0)

        for num, c in count.items():
            freq[c].append(num)


        # get the k elements
        res = []
        for key in range(len(freq)-1, 0, -1):
            for val in freq[key]:
                res.append(val)
                if len(res) == k: return res

        return res