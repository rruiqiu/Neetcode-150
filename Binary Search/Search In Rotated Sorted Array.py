class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check if the targe is between the sorted half, then

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:  # left sorted half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:  # not in the sorted half
                    l = mid + 1
            else:  # right half is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
