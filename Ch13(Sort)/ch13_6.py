def insertionSort(arr):
    n = len(arr)
    for end in range(1, n):
        # 마지막을 현재로 두고 함 이전 값과 비교
        for cur in range(end, 0, -1):
            if arr[cur - 1] > arr[cur]:
                # Swap
                arr[cur - 1], arr[cur] = arr[cur], arr[cur - 1]
    return arr


dataArray = [188, 162, 168, 120, 50, 150, 177, 105]
print(dataArray)
dataArray = insertionSort(dataArray)
print(dataArray)
