class Solution:
    def findMin(self, nums: List[int]) -> int:
        # search in sorted array

        # always search on the smaller sorted portion, nums[m] < nums[r]

        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res
