class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        max_count = 0

        for i in nums:
            freq[i] += 1
            max_count = max(max_count, freq[i])

        res = []
        for count in range(max_count, 0, -1):
            for key, value in freq.items():
                if value == count:
                    res.append(key)
                    if len(res) == k:
                        return res

        return res