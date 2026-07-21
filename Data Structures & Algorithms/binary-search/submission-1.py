class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower: int = 0
        higher: int = len(nums) - 1

        while lower <= higher:
            mid: int = (higher + lower) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                higher = mid - 1
            else:
                lower = mid + 1
        
        return -1
