class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        existingNumbers = {}
        for number in nums:
            try:
                return existingNumbers[number]
            except:
                existingNumbers[number] = True
        return False
         