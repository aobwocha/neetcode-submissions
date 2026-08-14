class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        result = list()
        s_pointer = 0
        while s_pointer < len(s):
            curr_s = s_pointer
            while curr_s < len(s) and s[curr_s] != '#':
                curr_s += 1
            
            word_len = int(s[s_pointer : curr_s])
            result.append(s[curr_s + 1 : curr_s + 1 + word_len])

            s_pointer = curr_s + 1 + word_len
        
        return result