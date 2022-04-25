class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = str(x)
        length = len(value)
        for i,item in enumerate(value):
            if item != value[length-i-1]:
                return False
        return True