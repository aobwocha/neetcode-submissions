class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(set(nums)) == k:
            return list(set(nums))
        
        result = []
        numFrequency = {}

        for num in nums:
            numFrequency[num] = 1 + numFrequency.get(num, 0)

            # Only introducing numbers not already in result needs processing
            if num not in result:
                
                # Building initial result list until k unique elements
                if len(result) < k:
                    result.append(num)
                
                # Replacing initial numbers in the list with higher freq numbers found later
                else:
                    for index in range(len(result)):
                        
                        # Finds number with a frequency less by 1 and replaces it
                        if numFrequency[result[index]] < numFrequency[num]:
                            result[index] = num
                            break
        return result


