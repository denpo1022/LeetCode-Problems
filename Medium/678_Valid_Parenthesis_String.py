class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i, e in enumerate(s):
            if e == '(':
                stack.append((i, e))
            elif e == '*':
                star.append((i, e))
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack:
            if star:
                if star[-1][0] > stack[-1][0]:
                    stack.pop()
                    star.pop()
                else:
                    return False
            else:
                return False
        return True