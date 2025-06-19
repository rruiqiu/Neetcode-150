from typing import List
from collections import Counter
"""
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # an array to count the freq
        nums_c = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]  # freq occur at most
        # put cooresponding count to the freq
        print(freq)
        for val, count in nums_c.items():
            freq[count].append(val)
        print(freq)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res

        # top k -> max heap
        # k most frequent
        # max_heap = []
        # one way is to count and return like a counter

        # nums_c = Counter(nums)
        # # return the k most, and convert it into a max heap
        # max_heap = []
        # for val, count in nums_c.items():
        #     heapq.heappush(max_heap, (-count,val))

        # res = []
        # for i in range(k):
        #     count, val = heapq.heappop(max_heap)
        #     res.append(val)

        # return res

        # another way is to maintain a window size heap
        # nums_c = Counter(nums)
        # #convert into a k size heap, then for the rest, compare if exists
        # res = []
        # for val,count in nums_c.items():
        #     heapq.heappush(res,(count,val))
        #     if len(res) > k:
        #         heapq.heappop(res)
        # final = []
        # for i in range(k):
        #     count, val = heapq.heappop(res)
        #     final.append(val)
        # return final
