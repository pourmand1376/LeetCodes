# https://leetcode.com/problems/combination-sum/
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       candidates = sorted(candidates)
       self.results = []
       self.sum_dfs(candidates, target, [])
       return self.results

    def sum_dfs(self, candidates: List[int], target: int, used_items: List[int]) -> List[List[int]]:
        if target < 0:
            return 
        if target == 0:
            return used_items
        
        for item in candidates:
            if len(used_items)>0 and used_items[-1] > item:
                continue
            result=self.sum_dfs(candidates, target - item, used_items + [item])
            if result:
                self.results.append(result)
    
print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))