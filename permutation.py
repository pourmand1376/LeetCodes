from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        permuted = []
        for index,item in enumerate(nums):
            new_list = nums[:index] + nums[index+1:]
            for permute_item in self.permute(new_list):
                permuted.append([item] + permute_item)

        return permuted
            
nums = [1,2,3]
print(Solution().permute(nums))
        
