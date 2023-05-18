# https://leetcode.com/problems/jump-game/
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_array = [False]*len(nums)
        jump_array[0] = True
        for i in range(1,len(nums)):
            for k in range(1,i+1):
                if jump_array[i-k] and nums[i-k]>=k:
                    jump_array[i] = True
                    break

        return jump_array[len(nums)-1]
    
print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))