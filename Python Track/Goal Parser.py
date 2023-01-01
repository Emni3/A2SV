class Solution:
    def interpret(self, command: str) -> str:
        interpreted = ""
        for i in range(len(command)):
            if command[i] == '(':
                if command[i+1] == ')':
                    interpreted  += 'o'
                    i += 2
                else:
                    interpreted += 'al'
                    i += 4
            #else: --> GoGalGGG
            elif command[i] == 'G':
                interpreted += 'G'
        return interpreted   
