class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'[':']', '(':')', '{':'}'}
        for item in s:
            if item in parentheses:
                stack.append(item)
            elif item in parentheses.values():
                if len(stack) == 0:
                    return False
                value=stack.pop()
                if parentheses[value] != item:
                    return False
        return stack == []
