# https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        for char in strs[0]:
            for word in strs:
                if not word.startswith(common+char):
                    return common
            common+= char
        return common

print(Solution().longestCommonPrefix(["flower","flow","flight"]))