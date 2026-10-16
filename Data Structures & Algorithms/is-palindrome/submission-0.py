class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

        lower_s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] not in valid_chars:
                left += 1
                continue

            if s[right] not in valid_chars:
                right -= 1
                continue

            if lower_s[left] != lower_s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True

            


        