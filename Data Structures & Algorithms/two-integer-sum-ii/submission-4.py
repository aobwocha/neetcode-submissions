class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        LEFT, RIGHT = 0, len(numbers) - 1
        while LEFT < RIGHT:
            two_sum = numbers[LEFT] + numbers[RIGHT]
            if two_sum == target:
                return [LEFT + 1, RIGHT + 1]
            elif two_sum > target:
                RIGHT -= 1
            else:
                LEFT += 1
        
        return []