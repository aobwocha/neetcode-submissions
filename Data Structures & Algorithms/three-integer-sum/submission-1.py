class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    currentJvalue = nums[j]
                    currentKvalue = nums[k]
                    while j < k and nums[j] == currentJvalue :
                        j += 1
                    while j < k and nums[k] == currentKvalue:
                        k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        
        return result
                