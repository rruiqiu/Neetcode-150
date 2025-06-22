class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Topics Monotonic decreasing queue
        # A deque that maintains the max element at the front and pop

        res = []
        dq = deque()

        l = 0
        for r, num in enumerate(nums):
            while dq and num > dq[-1]:
                # Compare from the decreasing queue from right to left
                dq.pop()
            dq.append(num)  # Always leave the smaller on the top

            if r >= k - 1:
                res.append(dq[0])
                if nums[l] == dq[0]:
                    dq.popleft()
                l += 1
        return res
