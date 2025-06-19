"""
Time complexity: O(n)
Space complexity: O(n)
"""

from collections import deque
from typing import List


class Solution:
    """Implements a solution for the sliding window maximum problem."""

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """Returns a list of maximums for each sliding window of size k."""

        res = []
        dq = deque()
        l = 0  # noqa: E741

        for r, num in enumerate(nums):
            # Maintain a decreasing deque;
            while dq and num > dq[-1]:
                dq.pop()  # remove all smaller elements from the back

            dq.append(num)

            if r >= k - 1:
                res.append(dq[0])
                if nums[l] == dq[0]:
                    dq.popleft()
                l += 1  # noqa: E741

        return res
