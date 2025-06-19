from typing import List
"""
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False
