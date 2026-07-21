class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Constraints: 
            - Provided a list
                - List contains integers
                - List is sorted in ascending order (with duplicates)

            - Return a list 
                - List contains integers
                - List is of length=2
                - List is such that index1 < index2
                - List is such that List[index1] + List[index2] = target
        
        For each integer, I need to check whether the complement exists. So
        the first idea is to calculate the complement, search the list, and if found,
        return their indices, if not, move to the next.
        '''

        for index, num in enumerate(numbers):
            complement = target - num
            for secondIndex, secondNum in enumerate(numbers[index+1:]):
                if secondNum == complement:
                    return [index+1, secondIndex+index+2]
        