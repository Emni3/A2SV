def countSwaps(a):
    # Write your code here
    sort_count = 0
    for i in range(len(a)):
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                sort_count += 1
    print("Array is sorted in", sort_count,"swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
