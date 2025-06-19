class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1 way is to use the hashmap, then similar to 2sums

        # but we can use sort to optimize it to O(1) space
        res = []
        nums.sort()
        print(nums)

        for i, num in enumerate(nums):
            # Avoid duplicates
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue # Skip duplicates

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1

        return res


