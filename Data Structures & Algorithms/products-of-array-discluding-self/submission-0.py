class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        length = len(nums)
        for i in range(length):
            result = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                result *= nums[j]
            answer.append(result)

        return answer
