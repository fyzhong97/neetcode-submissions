from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        @cache
        def dfs(idx):

            if idx >= n-1:
                return 0

            # if nums[idx] + idx >= n-1:
            #     return 1
            else:
                if nums[idx] == 0:
                    return float('inf')
            
            res = float('inf')
            for jump in range(1, nums[idx] + 1):
                res = min(res, 1 + dfs(idx + jump))
            
            return res

        return dfs(0)