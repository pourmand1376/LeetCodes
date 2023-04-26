# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words = sorted(words)
        sort_length = len(words) * len(words[0])

        result = []
        for index, word in enumerate(s):
            substring=s[index:index+sort_length]

            if len(substring) < sort_length:
                continue
            
            comparison_array = ([substring[i*len(value):(i+1)*len(value)] 
                                 for i,value in enumerate(words)])
            if sorted(comparison_array) == words:
                result.append(index)

        return result
    
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))
print(Solution().findSubstring( "barfoofoobarthefoobarman", ["bar","foo","the"]))