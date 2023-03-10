def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n+2)
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k
    maxi = 0
    prev = 0
    for i in arr:
        prev += i
        maxi = max(maxi, prev)
    return maxi
