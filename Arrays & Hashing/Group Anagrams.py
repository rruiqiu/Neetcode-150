from typing import List
from collections import defaultdict
"""
Time complexity: O(n), notice that freq(26) is constant
Space complexity: O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Freq 26
        hs = defaultdict(list)

        for each_str in strs:
            # counter
            freq = [0] * 26
            for char in each_str:
                freq[ord(char) - 97] += 1
            hs[tuple(freq)].append(each_str)
        print(hs)
        return list(hs.values())
