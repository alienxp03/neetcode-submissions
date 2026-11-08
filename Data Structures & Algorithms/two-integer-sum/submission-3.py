class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevMap:
                answer = [prevMap[diff], i]
                return answer
            prevMap[n] = i

        return []
