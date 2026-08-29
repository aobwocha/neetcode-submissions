class Solution:
    def findMin(self, nums: List[int]) -> int:
        LEFT, RIGHT = 0, len(nums) - 1
        res = nums[0]

        while LEFT <= RIGHT:
            if nums[LEFT] < nums[RIGHT]:
                return min(res, nums[LEFT])
            
            MID = (RIGHT + LEFT) // 2
            res = min(res, nums[MID])
            if nums[MID] >= nums[LEFT]:
                LEFT = MID + 1
            else:
                RIGHT = MID - 1
        
        return res
