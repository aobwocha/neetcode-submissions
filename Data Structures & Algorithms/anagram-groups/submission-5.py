class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_groups = defaultdict(list)

        for word in strs:
            key_list = [0 for _ in range(26)]
            for char in word:
                key_list[ord(char) - ord('a')] += 1
            
            key_tuple = tuple(key_list)
            word_groups[key_tuple].append(word)
        
        return [word_group for word_group in word_groups.values()]