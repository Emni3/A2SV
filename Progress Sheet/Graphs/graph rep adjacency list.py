# dictionary 
from collections import defaultdict
n = int(input())
k = int(input())
d = defaultdict(list)
def addEdge(u, v):
    d[u].append(v)
    d[v].append(u)
for i in range(k):
    row = list(map(int, input().split()))
    if row[0] == 1:
        addEdge(row[1], row[2])
        #print(d)
    else:
        for key,val in d.items():
            if key == row[1]:
                print(*val)
