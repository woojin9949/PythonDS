def selectionSort(arr):
    n = len(arr)
    # index 마지막 값음 비교할 다음 대상이 없기에 제외 n-2까지
    for i in range(0, n - 1):
        minIdx = i
        # index 다음 값부터 비교 n-1까지
        for k in range(i + 1, n):
            if arr[minIdx] > arr[k]:
                minIdx = k
        tmp = arr[i]
        arr[i] = arr[minIdx]
        arr[minIdx] = tmp
    return arr


dataArray = [188, 162, 169, 120, 50, 150, 177, 105]

print(dataArray)
dataArray = selectionSort(dataArray)
print(dataArray)
