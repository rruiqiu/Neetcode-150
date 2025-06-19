class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = Counter(t)
        window = defaultdict(int)

        needed = len(T)
        haved = 0

        min_len = float("inf")
        l = 0
        res = [-1, -1]

        for r, char in enumerate(s):
            if char in T:  # If a match
                window[char] += 1
                if window[char] == T[char]:
                    haved += 1

                while haved == needed:
                    # Update result
                    if (r - l + 1) < min_len:
                        min_len = r - l + 1
                        res = [l, r]

                    # Try to shrink window
                    left_char = s[l]
                    if left_char in T:
                        if window[left_char] == T[left_char]:
                            haved -= 1
                        window[left_char] -= 1
                    l += 1
        l, r = res
        if l != -1:
            return s[l : r + 1]
        else:
            return ""
