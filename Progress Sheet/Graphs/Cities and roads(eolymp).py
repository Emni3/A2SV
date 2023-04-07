from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    row = list(map(int, input().split()))
    for r in range(len(row)):
        if row[r] == 1:
            d[i+1] += 1
maxi = 0
for k,v in d.items():
    maxi = max(v, maxi)
print(maxi)
    
