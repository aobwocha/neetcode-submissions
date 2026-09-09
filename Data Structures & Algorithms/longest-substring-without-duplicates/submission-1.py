class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_substr = 0
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            max_substr = max(max_substr, r - l + 1)
        
        return max_substr