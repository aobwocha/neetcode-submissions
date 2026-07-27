class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        idx = 0
        result = list()
        while idx < len(s):
            len_idx = idx
            while s[len_idx] != "#":
                len_idx += 1
            
            length = int(s[idx:len_idx])
            result.append(s[len_idx + 1: len_idx + 1 + length])

            idx = len_idx + 1 + length
        
        return result
            