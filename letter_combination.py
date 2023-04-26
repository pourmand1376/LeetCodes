# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.phone_dict = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        return self.multiply(digits, "")

    
    def multiply(self, remaining_digits: str, to_now: str) -> List[str]:
        if len(remaining_digits) == 0:
            return [to_now] if len(to_now) > 0 else []

        results = []
        for value in self.phone_dict[remaining_digits[0]]:
            results.extend(self.multiply(remaining_digits[1:], to_now+value))
                    
        return results
        
print(Solution().letterCombinations('23'))
print(Solution().letterCombinations('2'))
print(Solution().letterCombinations(''))

