class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total, zeroCounter = 1, 0
        for num in nums:
            if num == 0: zeroCounter += 1
            else: total *= num
            
            if zeroCounter > 1: return [0 for _ in range(len(nums))]
                    
        result = []
        for num in nums:
            if zeroCounter == 1:
                if num != 0: result.append(0)
                else: result.append(total)
            else:
                result.append(total//num)

        return result
