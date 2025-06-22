class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # most intutive way is start searching from 0 until it exceeds the condition
        # start from lower increase by 1 till it stops

        max_k = max(piles)  # O(n)
        low = 1

        # modified binary search on the mininum
        def count_bananas(k):
            count = 0
            for pile in piles:
                if pile % k != 0:
                    count += pile // k + 1
                else:
                    count += pile // k
            print(count)
            return count

        min_k = -1
        while low <= max_k:
            mid = (low + max_k) // 2

            if count_bananas(mid) <= h:
                min_k = mid
                max_k = mid - 1
            else:
                low = mid + 1

        return min_k
