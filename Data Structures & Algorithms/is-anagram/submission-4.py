class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_counts = {}
        t_counts = {}

        if len(s) != len(t):
            return False

        for char in s:
            self.createOrIncrement(s_counts, char)

        for char in t:
            self.createOrIncrement(t_counts, char)

        for key, val in s_counts.items():
            if key not in t_counts or val != t_counts[key]:
                return False

        return True

    def createOrIncrement(self, char_counts: dict, ch: str):
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
