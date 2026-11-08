class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}

        for num in nums:
            if num in data:
                return True
            else:
                data[num] = 1

        return False

         
