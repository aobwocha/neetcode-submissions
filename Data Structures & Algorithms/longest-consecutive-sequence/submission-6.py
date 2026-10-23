class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq_len = 0

        for num in nums:
            if num - 1 in nums_set:
                continue
            
            seq_len = 0
            while num + seq_len in nums_set:
                seq_len += 1
            
            max_seq_len = max(max_seq_len, seq_len)
        
        return max_seq_len