class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for item in nums:
            freq[item] = freq.get(item, 0) + 1
        sorted_freq = sorted(freq, key= freq.get, reverse= True)
        return sorted_freq[:k]
        