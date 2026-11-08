class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        freq = [[] for _ in range(len(nums) +1)]

        for n in nums:
            hash[n] = 1 + hash.get(n, 0)

        for n, c in hash.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    result.sort()
                    return result
        return []
