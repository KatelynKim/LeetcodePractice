class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []
        for i in range(len(s)):

            if len(stack) == 0:
                stack.append(s[i])

            else:
                if s[i] in mapping and stack[-1] == mapping[s[i]]:
                    stack.pop()
                else:
                    stack.append(s[i])

        return len(stack) == 0


