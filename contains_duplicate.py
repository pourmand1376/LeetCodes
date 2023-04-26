# https://leetcode.com/problems/contains-duplicate/
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for item in nums:
            if item in visited:
                return True
            visited.add(item)
        return False

class FirstSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
