class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        l = 0
        for r, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(char)
            max_len = max(max_len, (r - l + 1))
        return max_len