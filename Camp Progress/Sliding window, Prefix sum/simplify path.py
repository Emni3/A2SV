class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        p = []
        for i in path:
            if i == '':
                continue
            p.append(i)
        #print(p)
        stack = []
        for i in p:
            if i == '..' and len(stack) > 0:
                stack.pop()
                continue
            elif i == '.' or i == '..':
                continue
            stack.append("/" + i)
        if len(stack) > 0:
            return ''.join(stack)
        return "/"
