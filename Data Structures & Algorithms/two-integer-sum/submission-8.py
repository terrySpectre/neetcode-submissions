class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = 1
        #nums_sort = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
        
