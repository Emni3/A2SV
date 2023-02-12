n, m = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
 
merged = []
i = 0
j = 0
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1
if i < len(lst1):
    while i < len(lst1):
        merged.append(lst1[i])
        i += 1
if j < len(lst2):
    while j < len(lst2):
        merged.append(lst2[j])
        j += 1
 
print(*merged)
