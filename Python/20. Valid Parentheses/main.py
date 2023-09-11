class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"(":")", "[":"]", "{": "}"}
        for i in s:
            if i in m.keys():
                stack.append(i)
            elif stack and i == m[stack[-1]]:
                stack.pop(-1)
            elif i in m.values():
                if not stack or i != m[stack[-1]]:
                    return False
        return len(stack) == 0