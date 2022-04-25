class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in ['(','{','[']:
                stack.append(item)
            elif item in [')','}',']']:
                if len(stack) == 0:
                    return False
                value=stack.pop()
                if value == '(' and item != ')' \
                or value == '{' and item != '}' \
                or value == '[' and item != ']':
                    return False
        return stack == []