import textwrap

def wrap(string, max_width):
    new = ""
    for i in range(0,len(string), max_width):
        new = new + string[i: i + max_width] + '\n'
        
    return new
    
        
        
        
        

if __name__ == '__main__':
