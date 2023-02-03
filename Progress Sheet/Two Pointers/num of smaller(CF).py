n, m = (map(int, input().split()))
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
 
first = 0
smallCount = []
 
for sec in range(m):
    while first < n and list1[first] < list2[sec]:
        first += 1
    smallCount.append(first)
print(*smallCount)
