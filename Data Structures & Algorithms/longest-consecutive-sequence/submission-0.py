class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        found_set = dict()
        max_found = 0
        for num in nums:
            if num in found_set: continue

            prev = num - 1
            nex = num + 1
            curr_seq = 1

            if prev in found_set and nex in found_set:
                curr_seq += found_set[prev] + found_set[nex]
                seq_start = prev + 1 - found_set[prev]
                seq_end = nex - 1 + found_set[nex]
                found_set[seq_start] = curr_seq
                found_set[seq_end] = curr_seq
            elif prev in found_set:
                curr_seq += found_set[prev]
                seq_start = prev + 1 - found_set[prev]
                found_set[seq_start] = curr_seq
            elif nex in found_set:
                curr_seq += found_set[nex]
                seq_end = nex - 1 + found_set[nex]
                found_set[seq_end] = curr_seq
            
            found_set[num] = curr_seq
            max_found = max(max_found, curr_seq)
        
        return max_found
