class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = dict()
        max_len = 0
        max_freq = 0

        l = 0
        for r, end_char in enumerate(s):
            counts[end_char] = counts.get(end_char, 0) + 1
            max_freq = max(max_freq, counts[end_char])

            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, (r - l + 1))

        return max_len