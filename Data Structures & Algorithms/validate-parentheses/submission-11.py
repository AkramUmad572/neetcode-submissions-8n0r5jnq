class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            elif ch == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif ch == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif ch == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        return not stack