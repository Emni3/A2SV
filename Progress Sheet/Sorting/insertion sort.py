def insertionSort1(n, arr):
    for i in range(1, len(arr)):
        curr_num = arr[i]
        j = i-1
        while j >= 0 and curr_num < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print(*arr)
        arr[j+1] = curr_num
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
