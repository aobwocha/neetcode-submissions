class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
            
        found_nums: set = set()
        for num in nums:
            if num in found_nums:
                return True
            found_nums.add(num)
        return False