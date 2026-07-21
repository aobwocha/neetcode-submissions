class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroCounter = 0

        result = []
        for num in nums:
            if num == 0:
                zeroCounter += 1
            else:
                total *= num
            
            if zeroCounter > 1:
                return [0 for _ in range(len(nums))]
                    

        for num in nums:
            if zeroCounter == 1:
                if num != 0:
                    result.append(0)
                else:
                    result.append(total)
            else:
                result.append(int(total/num))

        return result
