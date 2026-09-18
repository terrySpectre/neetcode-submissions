class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}

        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in hash_nums:
                return [hash_nums[num2], i]
            hash_nums[num] = i
            
        
