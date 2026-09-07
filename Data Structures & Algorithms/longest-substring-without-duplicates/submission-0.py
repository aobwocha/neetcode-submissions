class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r, curr_char in enumerate(s):
            while curr_char in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(curr_char)
            res = max(res, r - l + 1)
        
        return res