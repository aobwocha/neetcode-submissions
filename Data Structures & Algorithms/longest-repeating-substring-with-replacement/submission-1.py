class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0

        counts = dict()
        max_freq = 0

        l = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_freq = max(max_freq, counts[s[r]])

            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len