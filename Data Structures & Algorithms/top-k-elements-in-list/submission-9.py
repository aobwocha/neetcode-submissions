class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        counts_arr = [[] for _ in range(len(nums) + 1)]
        for val, count in counts.items():
            counts_arr[count].append(val)
        
        result = []
        for i in range(len(counts_arr) - 1, 0, -1):
            for val in counts_arr[i]:
                result.append(val)
            
            if len(result) == k: return result
                