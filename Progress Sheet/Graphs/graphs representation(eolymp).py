# matrix

from collections import defaultdict
n = int(input())
sink= []
source = []
d = defaultdict(int)
for r in range(1, n+1):
    row = list(map(int,input().split()))
    for i in range(len(row)):
        d[i+1] += row[i]
    
    if row.count(1) == 0:
        sink.append(r)
for i in d:
    if d[i] == 0:
        source.append(i)
source.sort()
sink.sort()
print(len(source),*source)
print(len(sink), *sink)  
