class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for i, num in enumerate(nums):
            if (num - 1) in nums_set: continue

            j = 0
            while (num + j) in nums_set:
                j += 1
            
            longest = max(longest, j)
        
        return longest