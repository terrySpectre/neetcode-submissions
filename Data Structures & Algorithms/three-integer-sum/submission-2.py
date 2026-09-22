class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                cur_sum = a + nums[L] + nums[R]
                if cur_sum > 0:
                    R -= 1
                elif cur_sum < 0:
                    L += 1
                else:
                    output.append([a, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return output
