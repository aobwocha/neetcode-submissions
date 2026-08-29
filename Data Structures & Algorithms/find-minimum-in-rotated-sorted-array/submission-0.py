class Solution:
    def findMin(self, nums: List[int]) -> int:
        RIGHT = len(nums) - 1
        LEFT = 0
        res = nums[0]

        while LEFT <= RIGHT:
            if nums[LEFT] < nums[RIGHT]:
                res = min(res, nums[LEFT])
                break
            
            MID = (RIGHT + LEFT) // 2
            res = min(res, nums[MID])

            if nums[MID] >= nums[LEFT]:
                LEFT = MID + 1
            else:
                RIGHT = MID - 1
        
        return res
