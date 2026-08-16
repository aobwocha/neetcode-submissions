class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = list()
        i = 0
        while i < len(nums):
            if nums[i] > 0: return result

            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        
        return result