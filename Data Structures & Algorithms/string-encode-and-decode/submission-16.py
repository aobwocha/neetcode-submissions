class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            
            len_word = int(s[l : r])
            word = s[r + 1 : r + 1 + len_word]
            res.append(word)

            l = r + 1 + len_word
        
        return res
