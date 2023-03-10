class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        if s.isdigit():
            return ""

        for i in s:
            if i != "]":
                stack.append(i)
            else:
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)* string)
                
        return "".join(stack)
