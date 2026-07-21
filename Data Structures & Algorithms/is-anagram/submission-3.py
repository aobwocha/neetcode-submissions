class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTracker = {}
        tTracker = {}
        
        for letter in s:
            try:
                sTracker[letter] += 1
            except:
                sTracker[letter] = 1
        
        for letter in t:
            try:
                tTracker[letter] += 1
            except:
                tTracker[letter] = 1

        for key, value in sTracker.items():
            try:
                if tTracker[key] != value:
                    return False
            except:
                return False
        
        for key, value in tTracker.items():
            try:
                if sTracker[key] != value:
                    return False
            except:
                return False
        return True
        