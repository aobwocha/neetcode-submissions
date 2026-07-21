class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNums = {}

        for index, num in enumerate(nums):
            pairNum = target - num
            if pairNum in pastNums.keys():
                return [pastNums[pairNum], index]
            else:
                pastNums[num] = index

