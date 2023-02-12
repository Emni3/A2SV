n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if k == 0:
    if arr[0] - 1 > 0:
        print(arr[0]-1)
    else:
        print(-1)
elif k == n:
    print(arr[-1])
elif arr[k] == arr[k - 1]:
    print(-1)
else:
    if arr[k]-1 > 0:
        print(arr[k]-1)
    else:
        print(-1)
