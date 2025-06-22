class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2  # always bst on the lower half
        if len(nums1) > len(nums2):
            A, B = nums2, nums1

        l, r = 0, len(A) - 1

        while True:
            mid = (l + r) // 2

            B_r = half - mid - 2  # cuz index starts 0

            A_left = A[mid] if mid >= 0 else float("-inf")
            A_right = A[mid + 1] if mid + 1 < len(A) else float("inf")
            B_left = B[B_r] if B_r >= 0 else float("-inf")
            B_right = B[B_r + 1] if B_r + 1 < len(B) else float("inf")

            # the condition when it is true and we can break
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 0:
                    print(A_left, B_left, A_right, B_right)
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return min(A_right, B_right)
                break
            elif B_left > A_right:
                l = mid + 1
            else:
                r = mid - 1

        return -1
