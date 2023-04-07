from collections import defaultdict
n = int(input())
d = defaultdict(list)
for i in range(n):
    row = list(map(int, input().split()))
    for r in range(len(row)):
        if row[r] == 1:
            d[i+1].append(r+1)
for key, val in d.items():
    print(len(val), *val)
