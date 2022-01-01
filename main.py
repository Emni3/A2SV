'''
decrement = 8
counter = 64
value = 65
for i in range(0, 5):
    for k in range(0, decrement):
        print(end=" ")

        for j in range(0, i+1):
            counter = counter + 1
            value = counter
            temp = value
        for j in range(0, i + 1):
            ch = chr(value)
            print(ch, end=" ")
            value = value - 1
            value = temp
            decrement = decrement - 2
'''

n = int(input())
for i in range(2):
    for j in range(n):
        print('#'*(n-1), end=' ')
    print()

