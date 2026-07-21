class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(word1: str, word2: str) -> bool:
            if len(word1) != len(word2):
                return False
            
            countWord1, countWord2 = {}, {}
            for letter in word1:
                countWord1[letter] = 1 + countWord1.get(letter, 0)
            for letter in word2:
                countWord2[letter] = 1 + countWord2.get(letter, 0)
            
            return countWord1 == countWord2
    
        result = [[strs[0]]]
        for word in strs[1:]:
            newAnagram = True
            for anagram in result:
                if isAnagram(anagram[0], word):
                    anagram.append(word)
                    newAnagram = False
            if newAnagram:
                result.append([word])
        return result