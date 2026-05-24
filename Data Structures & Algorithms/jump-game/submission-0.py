class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        curright = 0
        n = len(nums)

        for i,x in enumerate(nums):
            if curright >= i:
                curright = max(curright, i + x)
            else:
                return False
        # if curright >= n-1:
        #     return True

        return True