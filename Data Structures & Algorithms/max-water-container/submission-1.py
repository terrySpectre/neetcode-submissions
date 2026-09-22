class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        cur_area = 0
        L, R = 0, len(heights) - 1
        while L < R:
            depth = min(heights[L], heights[R])
            cur_area = depth * (R - L)
            if cur_area > max_area:
                max_area = cur_area
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return max_area    