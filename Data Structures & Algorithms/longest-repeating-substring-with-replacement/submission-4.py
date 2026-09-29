class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = dict()
        max_freq = 0
        max_len = 0
        l = 0
        for r, char in enumerate(s):
            count_dict[char] = 1 + count_dict.get(char, 0)
            max_freq = max(max_freq, count_dict[char])

            while (r - l + 1) - max_freq > k:
                count_dict[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, (r - l + 1))
        return max_len
