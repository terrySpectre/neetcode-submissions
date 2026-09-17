class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        appears = []
        if len(nums) == 0:
            return False
        else:  
            for i in nums:
                if i not in appears:
                    appears.append(i)
                else:
                    return True
            return False