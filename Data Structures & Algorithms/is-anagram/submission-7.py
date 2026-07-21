class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars: dict = dict()
        for s_char in s:
            s_chars[s_char] = s_chars.get(s_char, 0) + 1
        
        t_chars: dict = dict()
        for t_char in t:
            t_chars[t_char] = t_chars.get(t_char, 0) + 1
        
        for char, s_count in s_chars.items():
            if t_chars.get(char, 0) != s_count:
                return False
        
        for char, t_count in t_chars.items():
            if s_chars.get(char, 0) != t_count:
                return False
        
        return True
                    