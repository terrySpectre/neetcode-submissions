class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        L, R = 0, len(height) - 1
        max_l, max_r = height[L], height[R]

        while L < R:
            if max_l <= max_r:
                L += 1
                max_l = max(max_l, height[L])
                res += max_l - height[L]
            else:
                R -= 1
                max_r = max(max_r, height[R])
                res += max_r - height[R]         
        return res   