class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)
        
        results = []
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                results.append(j)
            
            if len(results) == k:
                return results