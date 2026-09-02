class Solution:
    def search(self, nums: List[int], target: int) -> int:
        LEFT, RIGHT = 0, len(nums) - 1

        while LEFT <= RIGHT:            
            MID = (RIGHT + LEFT) // 2
            if nums[MID] == target:
                return MID

            if nums[MID] >= nums[LEFT]:
                if nums[LEFT] > target or target > nums[MID]:
                    LEFT = MID + 1
                else:
                    RIGHT = MID - 1
            else:
                if nums[MID] > target or target > nums[RIGHT]:
                    RIGHT = MID - 1
                else:
                    LEFT = MID + 1

        return -1