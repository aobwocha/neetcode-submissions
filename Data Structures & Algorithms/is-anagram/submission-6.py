class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        for char in s:
            sCount[char] = sCount.get(char, 0) + 1
        
        tCount = {}
        for char in t:
            tCount[char] = tCount.get(char, 0) + 1
            if tCount[char] > sCount.get(char, 0):
                return False
        if tCount != sCount:
            return False
        return True
        