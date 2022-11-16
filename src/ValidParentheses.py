class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        compare = {0: None,
                    '(': ')',
                   '[': ']',
                   '{': '}'}
        stack = [0]
        for char in s:
            if char in compare:
                stack.append(char)
            elif compare[stack.pop()] != char:
                return False
        return stack == [0]


