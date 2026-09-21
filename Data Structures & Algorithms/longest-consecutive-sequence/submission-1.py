class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for num in num_set:
            if (num - 1) not in num_set:
                cur_num = num
                cur_seq = 1

                while (cur_num + 1) in num_set:
                    cur_num += 1
                    cur_seq += 1

                if cur_seq > max_seq:
                    max_seq = cur_seq

        return max_seq