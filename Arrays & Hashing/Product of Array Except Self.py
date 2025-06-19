from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # forward and backward
        # 1   2 3 4
        # 1 2 6 24 ->prefix
        # 24 12 12 4 ->postfix
        # the answer is equal to the prefix * postfix  except that index val output
        # so we can first store our prefix in res, then postfix to the current result O(1) time
        prefix, postfix = 1, 1
        res = [0] * len(nums)
        res[0] = prefix
        n = len(nums)
        for i in range(n):
            res[i] = prefix
            prefix = nums[i] * prefix

        for i in range(n - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res
