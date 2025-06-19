from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_table = {}

        for index, num in enumerate(nums):
            if target - num in num_table:
                return [num_table[target - num], index]
            else:
                num_table[num] = index
"""
Time complexity: O(n)
Space complexity: O(n)
"""