# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = dict() # char, last_appearance_index
        length = 0

        max_length = 0
        best_solution_set = None

        index = 0
        while index < len(s):
            if s[index] not in substring:
                substring[s[index]] = index
                length += 1
            else:
                if length > max_length:
                    best_solution_set = substring
                    max_length = length
                
                index = substring[s[index]]+1 # change to index last repeated character
                if index >= len(s):
                    break
                substring = {s[index]:index}
                length = 1
            
            if length > max_length:
                    best_solution_set = substring
                    max_length = length

            index = index + 1

        print(best_solution_set)
        return max_length


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring(" "))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("dvdf"))