class Solution:
    def findMin(self, nums: List[int]) -> int:
        LEFT, RIGHT = 0, len(nums) - 1
        min_num = nums[0]

        while LEFT <= RIGHT:
            if nums[LEFT] < nums[RIGHT]:
                min_num = min(min_num, nums[LEFT])
                break
            
            MID = (RIGHT + LEFT) // 2
            min_num = min(min_num, nums[MID])
            if nums[MID] >= nums[LEFT]:
                LEFT = MID + 1
            else:
                RIGHT = MID - 1
        
        return min_num