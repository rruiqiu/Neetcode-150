from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start with the num - 1, put the rest in  the set

        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:  # the start index
                count = 0
                while num in nums:
                    count += 1
                    num += 1
                longest = max(longest, count)

        return longest

"""
Time complexity: O(n)
Space complexity: O(n)
"""
