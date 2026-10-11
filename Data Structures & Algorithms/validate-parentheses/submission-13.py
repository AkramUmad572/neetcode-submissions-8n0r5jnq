class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for n in s:
            if stack and n == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and n == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and n == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(n)

        return not stack