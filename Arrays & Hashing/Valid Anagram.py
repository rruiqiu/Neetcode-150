from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter dict
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count
