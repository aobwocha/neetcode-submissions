class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in nums: continue

            curr_seq = 1
            while num + curr_seq in nums: 
                curr_seq += 1
            
            longest = max(longest, curr_seq)
        
        return longest