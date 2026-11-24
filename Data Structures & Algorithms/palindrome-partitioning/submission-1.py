class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, path):
            if i == len(s):
                res.append(path.copy())
                return
            

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    path.append(s[i : j + 1])
                    dfs(j + 1, path)
                    path.pop()
            
        dfs(0, [])
        return res
    
    def isPalindrome(self, s: str, i: int, j:int) -> bool:
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        
        return i >= j