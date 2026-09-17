class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        appear_s = {}
        appear_t = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in appear_s:
                appear_s[i] += 1
            else:
                appear_s[i] = 1
        for j in t:
            if j in appear_t:
                appear_t[j] += 1
            else:
                appear_t[j] = 1
        return appear_s == appear_t

            