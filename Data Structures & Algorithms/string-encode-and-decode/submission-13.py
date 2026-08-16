class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        result = list()
        i = 0
        while i < len(s):
            pointer = i
            while s[pointer] != '#':
                pointer += 1
            
            word_len = int(s[i : pointer])
            word = s[pointer + 1 : pointer + 1 + word_len]
            result.append(word)

            i = pointer + 1 + word_len
        
        return result