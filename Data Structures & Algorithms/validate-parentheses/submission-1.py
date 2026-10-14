class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {'(':')','{':'}','[':']'}
        for c in s:
            if c in list(m.keys()):
                stack.append(c)
            elif len(stack) == 0 or m[stack.pop()] != c:
                return False
        if len(stack) != 0:
            return False
        return True