class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i.lower()  
        L, R = 0, len(new_s) - 1
        while L < R:
            if new_s[L] != new_s[R]:
                return False
            L += 1
            R -= 1
        return True
