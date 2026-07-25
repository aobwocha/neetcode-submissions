class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)
        
        result = list()
        for idx in range(len(nums), 0, -1):
            for num in freq[idx]:
                result.append(num)
            
            if len(result) == k:
                return result