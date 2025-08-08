from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        freq_list = []
        for key in frequency:
            freq_list.append((frequency[key], key))

        freq_list = sorted(freq_list, reverse=True)

        result = []
        for i in range(k):
            result.append(freq_list[i][1])

        return result
