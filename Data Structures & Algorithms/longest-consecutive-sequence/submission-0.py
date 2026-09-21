class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        seen = set()
        for i in nums:
            if i in seen:
                continue
            seen.add(i)

        cur_seq = 1
        max_seq = 0    
        for j in sorted(seen):
            if j + 1 in seen:
                cur_seq += 1
            else:
                if cur_seq > max_seq:
                    max_seq = cur_seq
                cur_seq = 1
        return max_seq