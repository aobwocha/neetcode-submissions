class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        res = list()
        s_pointer = 0
        while s_pointer < len(s):
            curr_pointer = s_pointer
            while s[curr_pointer] != '#':
                curr_pointer += 1

            word_len = int(s[s_pointer : curr_pointer])
            res.append(s[curr_pointer + 1 : curr_pointer + 1 + word_len])

            s_pointer = curr_pointer + 1 + word_len
        
        return res