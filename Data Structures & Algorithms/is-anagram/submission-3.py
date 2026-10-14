class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_counts = {}
        t_counts = {}

        for char in s:
            self.createOrIncrement(s_counts, char)

        for char in t:
            if char not in s_counts:
                return False
            s_counts[char] -= 1

        for val in s_counts.values():
            if val != 0:
                return False

        return True

    def createOrIncrement(self, char_counts: dict, ch: str):
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
