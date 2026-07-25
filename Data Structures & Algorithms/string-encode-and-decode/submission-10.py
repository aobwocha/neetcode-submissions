class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = list()
        idx = 0
        while idx < len(s):
            len_tracker = idx
            while s[len_tracker] != '#':
                len_tracker += 1
            
            length = int(s[idx : len_tracker])
            res.append(s[len_tracker + 1 : len_tracker + 1 + length])
            idx = len_tracker + 1 + length

        return res