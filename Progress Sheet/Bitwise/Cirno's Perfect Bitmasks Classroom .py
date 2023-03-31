test = int(input())
for t in range(test):
    x = int(input())
    num = str(bin(x)[2:])
    i = len(num)-1
    while i >= 0:
        if num[i] == "1":
            break
        i -= 1
    
    shift =(len(num) - i) - 1
    
    y = (1 << shift)
   
    if y == x and shift > 0:
        y += 1
    elif shift == 0 and y == x:
        y += 2

    print(y)
        
