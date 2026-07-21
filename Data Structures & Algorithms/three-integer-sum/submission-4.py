class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()
        for idx, num in enumerate(nums):
            if idx != 0 and num == nums[idx - 1]: continue
            
            if num > 0: return result

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result
                
                