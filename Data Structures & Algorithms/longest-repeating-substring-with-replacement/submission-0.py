class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_freq = 0
        max_len = 0
        l = 0
        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])

            while l <= r and (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len