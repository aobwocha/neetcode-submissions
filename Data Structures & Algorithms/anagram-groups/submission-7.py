class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = defaultdict(list)
        for s in strs:
            char_key = [0] * 26
            for char in s:
                char_key[ord('a') - ord(char)] += 1
            
            grouped_words[tuple(char_key)].append(s)
        
        return [group for group in grouped_words.values()]