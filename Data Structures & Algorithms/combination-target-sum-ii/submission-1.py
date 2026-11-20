class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])

                cur.pop()
        
        dfs(0, [], 0)
        return res