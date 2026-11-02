class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}
        for i in range(len(nums)):
            complement = target - nums[i];
            if complement in indeces:
                return [indeces[complement], i]
            indeces[nums[i]] = i
        
        
