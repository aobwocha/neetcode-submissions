class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()

        INDEX = 0
        while INDEX < len(nums):
            if INDEX > 0 and nums[INDEX] == nums[INDEX - 1]: 
                INDEX += 1
                continue

            if nums[INDEX] > 0: return result

            LEFT, RIGHT = INDEX + 1, len(nums) - 1
            while LEFT < RIGHT:
                three_sum = nums[INDEX] + nums[LEFT] + nums[RIGHT]
                if three_sum == 0:
                    result.append([nums[INDEX], nums[LEFT], nums[RIGHT]])
                    LEFT += 1
                    while LEFT < RIGHT and nums[LEFT] == nums[LEFT - 1]:
                        LEFT += 1
                elif three_sum > 0:
                    RIGHT -= 1
                else:
                    LEFT += 1
            
            INDEX += 1
        
        return result
