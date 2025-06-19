class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #
        l, r = 0, 1
        remain = k
        char_most = s[l]
        replace_queue = deque()
        max_len = 0

        while r < len(s):
            # print(s[r])
            if s[r] == char_most:
                r += 1
            elif s[r] != char_most and remain > 0:
                replace_queue.append(r)
                r += 1
                remain -= 1
            else:
                if replace_queue:
                    l = replace_queue.popleft()
                else:
                    l = r
                r = l + 1
                char_most = s[l]
                remain = k

            max_len = max(max_len, r - l)

        return max_len
