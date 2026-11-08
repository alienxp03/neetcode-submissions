class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            rem = target - num
            if rem in dic:
                return [dic[rem], i]
            dic[num] = i
            
