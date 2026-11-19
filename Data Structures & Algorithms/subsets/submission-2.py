class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, cur):
            if idx >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[idx])
            dfs(idx + 1, cur)

            cur.pop()
            dfs(idx + 1, cur)
        
        dfs(0, [])
        return res