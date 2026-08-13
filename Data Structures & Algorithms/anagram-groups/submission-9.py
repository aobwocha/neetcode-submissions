class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = collections.defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            key = tuple(key)
            grouped_words[key].append(word)
        
        return [val for val in grouped_words.values()]
