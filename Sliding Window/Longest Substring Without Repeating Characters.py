class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maintain a set for duplicates
        # visited_char = set()
        # l = 0
        # max_len = 0

        # for r, char in enumerate(s):
        #     while char in visited_char:
        #         visited_char.remove(s[l])
        #         l += 1

        #     visited_char.add(char)
        #     max_len = max(max_len, r - l + 1)

        # return max_len
        # #to further optimize, we can even use a hashmap to record the index, so we can use it to update the most leftg

        mp = {}
        l = 0
        max_len = 0

        for r, char in enumerate(s):
            if char in mp:
                # The left pointer would be either the current one or the one that appears faster than the current one
                l = max(mp[char] + 1, l)
            mp[char] = r
            max_len = max(max_len, r - l + 1)
        return max_len
