class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s: str, t: str) -> bool:
            s_chars = dict()
            for s_char in s:
                s_chars[s_char] = s_chars.get(s_char, 0) + 1
            
            t_chars = dict()
            for t_char in t:
                t_chars[t_char] = t_chars.get(t_char, 0) + 1
            
            for s_char, s_count in s_chars.items():
                if t_chars.get(s_char, 0) != s_count:
                    return False
            
            for t_char, t_count in t_chars.items():
                if s_chars.get(t_char, 0) != t_count:
                    return False
            
            return True
        
        result = []
        found_anagram = False
        for word in strs:            
            for index, word_group in enumerate(result):
                found_anagram = is_anagram(word_group[0], word)
                if found_anagram:
                    result[index].append(word)
                    break
            
            if not found_anagram:
                result.append([word])
        
        return result