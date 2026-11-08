class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicts = {}
        for n in nums:
            if n in dicts:
                return True
            dicts[n] = 1
        return False